## Kaizala Python API

Environment variables:

* mobile-number : Your mobile number which will be used for invoking apis
* application-id : ID associated with the Connector
* application-secret : Secret associated with the Connector

To create the variables:
* Navigate to Kaizala Management Portal @ https://manage.kaiza.la/
* Log in using an existing Office365 account
  * Tap on "Connectors" in the left menu
  * Tap on "Add Connector"
  * Register a connector for the 3rd party system that will use the API
  * Enter the name of the Connector and other details. Tap on Continue
  * Select permissions that is intended for the Connector to have access to
  * Tap on Create Connector

**IMPORTANT: Note the ID & Secret that get generated and displayed on the portal**

### Autentication
 - [ ] Generate PIN
 - [ ] Login with PIN and applicationID to get refreshToken
 - [ ] Retrieve the access token
 - [ ] Get loggedin user details

### Upload Media
- [ ] Upload media (image / document / audio / album/ video)
- [ ] Upload media URL (image / document / audio / album/ video)

### Group Management
- [ ] Create a group
- [ ] Fetch groups
- [ ] Fetch groups with details
- [ ] Add members to a group
- [ ] Query members of a group
- [ ] Remove members from a group

### Bots
- [ ] Create bot user
- [ ] Get bot users
- [ ] Generate accessToken for bot user
- [ ] Update bot user
- [ ] Delete bot user

reference:
https://docs.microsoft.com/en-us/kaizala/connectors/api
