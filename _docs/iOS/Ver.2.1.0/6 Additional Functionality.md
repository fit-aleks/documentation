---
title: "Additional Functionality"
permalink: ios_ver_2.1.0_additional_functionality.html
sidebar: mps_side_bar
---

Please check the section ‘Best Practices’ to understand the proper approach to implement this functionality.

## 1. Get MPS Site Config
To get MPS Site Config JSON, use

```swift
    mps.getSiteConfig(success: { (config) in
        
    }) { (error) in
        
    }
```

```objc
    [mps getSiteConfigWithSuccess:^(NSDictionary<NSString *,id> * _Nonnull json) {
        
    } failure:^(NSError * _Nonnull error) {
        
    }];
```

It returns the MPS Site Config JSON from MPS Server or an error.

## 2. Additional Targeting

To set page level custom targeting, pass the additionalTargeting argument on an ad request with a dictionary of custom targeting information. Additional targeting will be added to the ad targeting parameters from MPS Page JSON. 

### For Banner Ad:

```swift
    let customTargeting = ["targetingKey": "targeting-value", "targetingKey2": "targeting-value2"];
    page.getBannerAd(adUnit: "testbox", additionalTargeting: customTargeting, rootViewController: self, success: { [weak self] (ad) in
        if let sSelf = self {
            sSelf.view.addSubview(ad)
        }
    }) { (error) in
        print(error.localizedDescription)
    }
```

```objc
    NSDictionary *customTageting = @{@"key1": @"value1"};
    [page getBannerAdWithAdSlot:@"testbox" additionalTargeting:customTageting rootViewController:self success:^(MPSBannerAdView * _Nonnull ad) {
        
    } failure:^(NSError * _Nonnull error) {
        
    }];
```

### For Banner View:

```swift
    let params = MPSPageParameters(path: "page")
    params.cat = "someCatValue"
    
    let page = mps.requestPageObject(mpsParams: params)
    let targeting = ["targetingKey": "targeting-value"]
    adView.delegate = self
    adView.displayBannerAd(adSlot: "testbox", additionalTargeting: targeting, page: page, rootViewController: self)
```

```objc
    NSDictionary *customTageting = @{@"key1": @"value1"};
    [bannerView displayBannerAdWithAdSlot:@"testbox" page:page additionalTargeting:customTageting rootViewController:self];
```

### For Interstitial:

```swift 
    let targeting = ["targetingKey": "targeting-value"]
    page.getInterstitialAd(adUnit: "testinterstitial", additionalTargeting: targeting, success: { [weak self] (inter) in
        if let sSelf = self {
            inter.present(fromRootViewController: sSelf)
        }
    }) { (error) in
        print(error.localizedDescription)
    }
```

```objc
    NSDictionary *customTageting = @{@"key1": @"value1"};
    [page getInterstitialAdWithAdSlot:@"testinterstitial" additionalTargeting:customTageting success:^(MPSInterstitialAd * _Nonnull inter) {
        
    } failure:^(NSError * _Nonnull error) {
        
    }];
```