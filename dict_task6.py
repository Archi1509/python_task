def marketing_conversion(data):
    marketing_channels = {channel: rate for channel, rate in
                          sorted(marketing_performance.items(), key=lambda ele: ele[1], reverse=True)}
    highest_marketing_channel = dict(list(marketing_channels.items())[:1])
    print(highest_marketing_channel.items())

    avg_marketing_performance = {}
    count = 0
    sum = 0
    for channel, rate in marketing_performance.items():
        if channel not in avg_marketing_performance:
            count += 1
            sum += rate
    avg = sum / count
    print(f"Average Conversion Rate: {avg}%")


marketing_performance = {
    "Facebook Ads": 3.2,
    "Google Ads": 4.8,
    "Email Marketing": 2.5,
    "Organic Search": 5.6,
    "Referral": 3.9
}
marketing_conversion(marketing_performance)


