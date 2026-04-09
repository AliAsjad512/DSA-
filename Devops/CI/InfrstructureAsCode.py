import subprocess
import json
import argparse
import sys
import os
from pathlib import Path

class IaCValidator:
    def __init__(self, template_path):
        self.template_path = Path(template_path)

    def validate_cloudformation(self):
        """Validate CloudFormation template"""
        try:
            # Use aws cli to validate
            result = subprocess.run(
                ['aws', 'cloudformation', 'validate-template', '--template-body', f'file://{self.template_path}'],
                capture_output=True,
                text=True,
                check=True
            )
            return {'valid': True, 'message': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'valid': False, 'message': e.stderr, 'error': e.returncode}
        except FileNotFoundError:
            # Fallback: use cfn-lint if available
            try:
                result = subprocess.run(
                    ['cfn-lint', str(self.template_path)],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    return {'valid': True, 'message': 'Template passed cfn-lint'}
                else:
                    return {'valid': False, 'message': result.stdout + result.stderr}
            except:
                return {'valid': False, 'message': 'AWS CLI not found and cfn-lint not installed'}
    def validate_terraform(self):
        """Validate Terraform configuration"""
        # Terraform expects to be run in a directory with .tf files
        tf_dir = self.template_path if self.template_path.is_dir() else self.template_path.parent
        try:
            # terraform init first (quiet)
            subprocess.run(['terraform', 'init', '-backend=false'], cwd=tf_dir, capture_output=True, check=True)
            # terraform validate
            result = subprocess.run(['terraform', 'validate', '-no-color'], cwd=tf_dir, capture_output=True, text=True, check=True)
            return {'valid': True, 'message': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'valid': False, 'message': e.stderr}
        except FileNotFoundError:
            return {'valid': False, 'message': 'Terraform not installed'}
    def validate(self, type_='auto'):
        """Auto-detect template type"""
        if type_ == 'cloudformation' or (type_ == 'auto' and self.template_path.suffix in ['.yaml', '.yml', '.json']):
            return self.validate_cloudformation()
        elif type_ == 'terraform' or (type_ == 'auto' and self.template_path.suffix == '.tf'):
            return self.validate_terraform()
        else:
            return {'valid': False, 'message': f'Unknown template type: {type_}'}
        
    if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IaC Validator')
    parser.add_argument('template', help='Path to template file or directory')
    parser.add_argument('--type', choices=['auto', 'cloudformation', 'terraform'], default='auto')
    args = parser.parse_args()

    validator = IaCValidator(args.template)
    result = validator.validate(args.type)
    if result['valid']:
        print(f"✅ Template is valid")
        if result.get('message'):
            print(result['message'])
        sys.exit(0)
    else:
        print(f"❌ Template validation failed:")
        print(result['message'])
        sys.exit(1)
