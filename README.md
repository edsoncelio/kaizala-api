## Kaizala API

Microsoft Kaizala is a mobile app and service designed for large group communications and work management. 

---
**Environment variables:**

* **mobile-number** : Your mobile number which will be used for invoking apis
* **application-id** : ID associated with the Connector
* **application-secret** : Secret associated with the Connector
* **endpoint-url**: Response at `/accessToken` 
* **root-url**: https://api.kaiza.la/v1
* **refreshToken**: Response at `/accessToken` 
* **accessToken**: Response at `/accessToken` 

**To create an Connector:**
* Navigate to Kaizala Management Portal https://manage.kaiza.la/
* Log in using an existing Office365 account
  * Tap on "Connectors" in the left menu
  * Tap on "Add Connector"
  * Register a connector for the 3rd party system that will use the API
  * Enter the name of the Connector and other details. Tap on Continue
  * Select permissions that is intended for the Connector to have access to
  * Tap on Create Connector

**IMPORTANT: Note the ID & Secret that get generated and displayed on the portal**

### Autentication
 - [x] Generate PIN
 - [x] Login with PIN and applicationID to get refreshToken
 - [x] Retrieve the access token
 - [x] Get loggedin user details

### Upload Media
- [x] Upload media (image / document / audio / album/ video)
- [x] Upload media URL (image / document / audio / album/ video)

### Group Management
- [x] Create a group
- [x] Fetch groups
- [x] Fetch groups with details
- [x] Add members to a group
- [x] Query members of a group
- [x] Remove members from a group

### Content Creation APIs
 - [x] Send message on a group
 - [x] Send image on a group
 - [x] Send document on a group
 - [x] Send audio on a group
 - [x] Send video on a group
 
### Subscription APIs (webhooks)
- [x] Subscribe to all events at group level
- [x] Subscribe to all events at action level
- [x] Get all webhooks on a group
- [x] Unsubscribing a webhook

### Bots
- [x] Create bot user
- [x] Get bot users
- [x] Generate accessToken for bot user
- [x] Update bot user
- [x] Delete bot user

### Future work
- [ ] Add examples

Reference:

1. https://docs.microsoft.com/en-us/kaizala/connectors/api
2. https://docs.microsoft.com/en-us/rest/kaizala/
