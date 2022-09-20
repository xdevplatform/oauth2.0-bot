# Creating a Twitter bot with OAuth 2.0 and v2 of the Twitter API

Bots on Twitter are what makes the conversation on Twitter so lively. There are many unique bots on Twitter, from [tiny aquariums](https://twitter.com/EmojiAquarium) to warning you of [sewer overflow in NYC](https://twitter.com/combinedsewer). Bots make Twitter unique and engaging.

When our team launched the manage Tweets endpoints, I built a bot [@FactualCat](https://twitter.com/factualcat?lang=en) that Tweeted cat facts daily. This bot used OAuth 1.0a to authenticate, but I wanted to challenge myself to create a bot that used [OAuth 2.0 Authorization Code Flow with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code).

Since I was used to the OAuth 1.0a authentication flow, I had a hard time figuring out exactly what I needed to do to authenticate on behalf of my bot and get it running so that it could make requests regularly.

This code sample will allows you to make a bot similar to [@Factual__Dog](https://twitter.com/Factual__Dog), a bot that Tweets dogs facts twice daily. By the end of this tutorial, you should be able to create a Twitter bot that utilizes [OAuth 2.0 Authorization Code Flow with PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code) for authentication.

## Prerequisites

* A developer account.
  * If you don’t already have access to the Twitter API, [you can sign up for a developer account.](http://t.co/signup)
* A Project in the [developer portal](https://developer.twitter.com/en/portal/dashboard)
* An App containing the credentials required to use the Twitter API
* OAuth 2.0 turned on in your App’s authentication settings


## Tutorial 
To learn more about this code sample, check out [our tutorial which walks you through the steps to create this bot](https://developer.twitter.com/en/docs/tutorials/creating-a-twitter-bot-with-python--oauth-2-0--and-v2-of-the-twi).
