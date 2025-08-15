# WordPress OSINT
WordPress is a widely used content management system (CMS), and as such, it can be a valuable target for OSINT investigations. Gathering information about a WordPress site can help identify potential vulnerabilities, enumerate users, plugins, themes, and more.

## Common WordPress OSINT Techniques

- **Discovering if a site uses WordPress:**  
  Look for `/wp-content/`, `/wp-includes/`, or `/wp-admin/` in URLs or page source.

- **Enumerating Users:**  
  Try appending `/?author=1`, `/?author=2`, etc., to the site URL to reveal usernames.

- **Enumerating User info:**
 Try appending `/wp-json/wp/v2/users` to the site URL to get a list of users and their details.

- **Identifying Plugins and Themes:**  
  Check the HTML source for `/wp-content/plugins/` and `/wp-content/themes/` paths.

- **Checking WordPress Version:**  
  Look for a `meta name="generator"` tag in the HTML source or read `/readme.html` if accessible.

- **Finding Exposed Files:**  
  Attempt to access `/wp-config.php~`, `/wp-config.bak`, or backup files.

## Useful Tools

- [WPScan](https://github.com/wpscanteam/wpscan)  
  A popular tool for scanning WordPress sites for vulnerabilities, enumerating users, plugins, and more.

- [WhatWeb](https://github.com/urbanadventurer/WhatWeb)  
  Identifies websites, including WordPress and its plugins.

- [Wappalyzer](https://www.wappalyzer.com/)  
  Browser extension and online tool to detect CMS, plugins, and technologies used by a website.

- [CMSeeK](https://github.com/Tuhinshubhra/CMSeeK)  
  CMS detection and exploitation suite.
