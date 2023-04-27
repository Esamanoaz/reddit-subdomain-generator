# Reddit subdomain list & generator
 
Creates a text file containing all 676 two-letter `reddit.com` subdomains. This list includes localhost redirects so you can copy and paste it directly into a hosts file to block all the listed domains.

## Additional domains to block
In order to block `reddit.com` completely, you'll also need to include the following lines in your host file:
* `127.0.0.1 reddit.com`
* `127.0.0.1 old.reddit.com`
* `127.0.0.1 new.reddit.com`