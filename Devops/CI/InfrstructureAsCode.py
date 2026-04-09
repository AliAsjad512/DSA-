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
