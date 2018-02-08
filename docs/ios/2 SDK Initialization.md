# Initialization

You are now ready to create an MPS instance for requesting banner and interstitial ads.  

First, open your **ViewController.swift** or **ViewController.m** files (Swift and Objective-C respectively) and add **import nbcu_mps_ios_sdk** to access the SDK's public API methods.

```swift
import nbcu_mps_ios_sdk
```

```objc
@import nbcu_mps_ios_sdk;
```

You can now create an instance of MPS with the appropriate host URL and site by initializing the library. You can also specify the log level for this instance. Refer to **MPSSDKLogLevel** in the documentation for more details.  

Add the following code in your **ViewController.swift** file:

```swift
var mps: MPS!
override func viewDidLoad() {
    // explicit with base URL
    let url = URL(string: "https://mps.nbcuni.com")!
    let site = "test-sdk"
    
    let opt = MPSOptions()
    opt.logLevel = .debug

    mps = MPS(url: url, site: site, options: opt)
}
```
Or, add this code to your **ViewController.m** file,

```objc
@interface AppDelegate ()
{
    MPS *mps;
}

- (void)viewDidLoad {
    // explicit with base URL
    NSURL *url = [NSURL URLWithString:@"https://mps.nbcuni.com"];
    NSString *site = @"test-sdk";
    
    MPSOptions *opts = [[MPSOptions alloc] init];
    opts.logLevel = [MPSSDKLogLevel debug];
    mps = [[MPS alloc] initWithUrl: url site: site options:opts];
}
```

## Request an MPSPage Object

The MPS library operates with the concept of an MPSPage, which is similar to one web page. 
You will use this MPSPage object to request ads. 

To achieve this we create an instance of MPSPageParameters which facilitates building the request that will be sent to MPS. The list of all configurable properties are presented in the library documentation. 

For example:

```swift
var mps: MPS!
var page: MPSPage!
override func viewDidLoad() {
    super.viewDidLoad()
    let url = URL(string: "https://mps.nbcuni.com")!
    let site = "test-sdk"
    mps = MPS(url: url, site: site)

    let params = MPSPageParameters(path: "TEST")
    page = mps.requestPageObject(params: param, rootViewController: self)
```

```objc
@interface ViewController ()
{    
    MPS *mps;
    MPSPage *page;
}

- (void)viewDidLoad {
    [super viewDidLoad];

    NSURL *url = [NSURL URLWithString:@"https://mps.nbcuni.com"];
    NSString *site = @"test-sdk";
    mps = [[MPS alloc] initWithUrl:url site:site];

    MPSParameters *params = [[MPSParameters alloc] initWithPath:@"page"];
    page = [mps requestPageObject: param, rootViewController: self];
```

At this point you should be ready to build and run your application in your simulator. 

Next we will work on requesting banner and interstital ads, and adding them to the view hierarchy.
