# WHOIS

**WHOIS is a protocol that can be used for extracting information about a domain name or IP address.** It is useful for a wide array of purposes during an OSINT investigation and can give a wealth of information about a particular target. 

## Types of Information

WHOIS may give a variety of information, including (but not limited to):
- The domain registrar.
- The expiration date of the registry.
- When the domain was first created.
- When the domain was last updated.
- The individual or company registrant.
- The country of the registrant.
- The state or province of the registrant.
- The city of the registrant.
- The street address of the registrant.
- The postal code of the registrant.
- The registrant's email address.
- The registrant's phone number.
- The registrant's fax number.

## Using WHOIS

The most common way of using the WHOIS protocol to find information about a target is through the `whois` command-line utility.

```
$ whois <domain>
```

For example:

```
$ whois google.com
$ whois facebook.com
```
