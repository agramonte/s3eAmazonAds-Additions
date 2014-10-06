#include "GameLayer.h"
static int g_AdId;
static int g_InterstatialId;
static bool g_requestNewInterstatial;

static int32 _adBanner(void *systemData, void *userData)
{
    CCLog("---------------------------Ad Timer.");
    
    //Timer done. Request and load a new banner ad.
    s3eAmazonAdsLoadAd(g_AdId);
    
    if (g_requestNewInterstatial) {
        //
        //And request a new one.
        //
        s3eAmazonAdsLoadInterstitialAd(g_InterstatialId);
        
        //Change the interstatial flag back.
        g_requestNewInterstatial = false;
    }
    
    
    s3eTimerSetTimer(30000, _adBanner, NULL);
    return 0;
}

static int32 onAdError(void* systemData, void* userData)
{
    s3eAmazonAdsCallbackErrorData* data = static_cast<s3eAmazonAdsCallbackErrorData*>(systemData);
    
    if (data == NULL)
    {
        return 1;
    }
    CCLog("---------------------------Ad failed to load. Error: %s.", data->m_Error);

    return 0;
}

static int32 onAdLoad(void* systemData, void* userData)
{
    s3eAmazonAdsCallbackLoadedData* data = static_cast<s3eAmazonAdsCallbackLoadedData*>(systemData);
    CCLog("---------------------------Ad loaded.");
    
    if (data == NULL || data->m_Properties == NULL)
    {
        return 1;
    }
    
    if (data->m_Id == g_InterstatialId) {
        //
        //Once it is available show the interstatial or you can wait until necessary (scene change or end of round).
        //
        s3eAmazonAdsShowAd(g_InterstatialId);
        
    }
    
    //
    //Change the flag so at the next interval you can request a new one.
    g_requestNewInterstatial = true;
    
    return 0;
}

GameLayer::~GameLayer()
{
    
}

CCScene* GameLayer::scene()
{
    // 'scene' is an autorelease object
    CCScene *scene = CCScene::create();
    
    // 'layer' is an autorelease object
    GameLayer *layer = GameLayer::create();

    // Add layer as a child to scene
    scene->addChild(layer);

    // Return the scene
    return scene;
}

// on "init" you need to initialize your instance
bool GameLayer::init()
{
    if (!CCLayer::init())
        return false;

    // Create main loop
    this->schedule(schedule_selector(GameLayer::update));
    
    

    // COCOS2D TIP
    // Create Cocos2D objects here
    
    
    if (s3eAmazonAdsAvailable()) {
        
        g_AdId = 0;
        g_InterstatialId = 0;
        g_requestNewInterstatial = false;
        
        //
        //Use this for testing.
        //
        s3eAmazonAdsInit("your id here", true, true);
        
        //
        //Use this for production.
        //
        //s3eAmazonAdsInit("your id here", false, false);
        
        
        //Add the callbacks.
        s3eAmazonAdsRegister(S3E_AMAZONADS_CALLBACK_AD_ERROR,  onAdError,  this);
        s3eAmazonAdsRegister(S3E_AMAZONADS_CALLBACK_AD_LOADED, onAdLoad,  this);
        
        //Prepare the ads.
        s3eAmazonAdsPrepareAd(&g_AdId);
        s3eAmazonAdsPrepareAd(&g_InterstatialId);
        
        //
        //Use this for banner bottom
        //
        s3eAmazonAdsPrepareAdLayout(g_AdId, S3E_AMAZONADS_POSITION_BOTTOM, S3E_AMAZONADS_SIZE_AUTO);
        
        //
        //Use this for banner top
        //
        //s3eAmazonAdsPrepareAdLayout(adId, S3E_AMAZONADS_POSITION_TOP, S3E_AMAZONADS_SIZE_AUTO);
        
        //Load the ad.
        s3eAmazonAdsLoadAd(g_AdId);
        
        //Load the interstatial.
        s3eAmazonAdsLoadInterstitialAd(g_InterstatialId);
        
        //Banner ad change timer.
        s3eTimerSetTimer(30000, _adBanner, NULL);
        
        
    }

	// Create Box2D world
	world = new b2World(b2Vec2(0, 100));

    // BOX2D TIP
    // Create Box2D objects here

    return true;
}

void GameLayer::draw()
{
}

void GameLayer::update(float dt)
{
	// Update Box2D world
	world->Step(dt, 6, 3);

    // BOX2D TIP
    // Update objects from box2d coordinates here
}

