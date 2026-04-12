import boto3
import datetime
import json
import argparse
import numpy as np
from collections import defaultdict

class CostAnomalyDetector:
    def __init__(self, region='us-east-1'):
        self.ce = boto3.client('ce', region_name=region)

    def get_daily_costs(self, days_back=30):
        """Retrieve daily costs for last N days"""
        end = datetime.date.today()
        start = end - datetime.timedelta(days=days_back)
        response = self.ce.get_cost_and_usage(
            TimePeriod={
                'Start': start.strftime('%Y-%m-%d'),
                'End': end.strftime('%Y-%m-%d')
            },
            Granularity='DAILY',
            Metrics=['UnblendedCost'],
            GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
        )
        daily_data = defaultdict(dict)
        for result in response['ResultsByTime']:
            date = result['TimePeriod']['Start']
            for group in result['Groups']:
                service = group['Keys'][0]
                cost = float(group['Metrics']['UnblendedCost']['Amount'])
                daily_data[date][service] = cost
        return daily_data
    
    def detect_anomalies(self, days_back=30, threshold=2.0):
        """Detect anomalies using z-score (2 standard deviations)"""
        daily = self.get_daily_costs(days_back)
        total_by_day = {date: sum(services.values()) for date, services in daily.items()}
        dates = list(total_by_day.keys())
        costs = list(total_by_day.values())

        if len(costs) < 7:
            return []

        # Calculate moving average and std
        window = 7
        anomalies = []
        for i in range(window, len(costs)):
            window_costs = costs[i-window:i]
            mean = np.mean(window_costs)
            std = np.std(window_costs)
            current = costs[i]
            z_score = (current - mean) / std if std > 0 else 0
            if abs(z_score) > threshold and current > mean * 1.5:
                anomalies.append({
                    'date': dates[i],
                    'cost': current,
                    'expected': mean,
                    'z_score': round(z_score, 2),
                    'percentage_increase': round((current - mean) / mean * 100, 1)
                })

        return anomalies
    
     def get_top_services_for_date(self, date, daily_data):
        """Get top cost contributors for a given date"""
        if date not in daily_data:
            return []
        services = daily_data[date]
        sorted_services = sorted(services.items(), key=lambda x: x[1], reverse=True)
        return [{'service': s, 'cost': c} for s, c in sorted_services[:5]]
    
     if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AWS Cost Anomaly Detector')
    parser.add_argument('--days', type=int, default=30)
    parser.add_argument('--threshold', type=float, default=2.0)
    args = parser.parse_args()

    detector = CostAnomalyDetector()
    anomalies = detector.detect_anomalies(args.days, args.threshold)
    daily_data = detector.get_daily_costs(args.days)

    if anomalies:
        print(f"⚠️ Cost Anomalies Detected (last {args.days} days):")
        for a in anomalies:
            print(f"\n📅 {a['date']}: ${a['cost']:.2f} (expected ${a['expected']:.2f}, +{a['percentage_increase']}%)")
            print(f"   Top services that day:")
            top = detector.get_top_services_for_date(a['date'], daily_data)
            for svc in top:
                print(f"     - {svc['service']}: ${svc['cost']:.2f}")
    else:
        print("✅ No cost anomalies detected")