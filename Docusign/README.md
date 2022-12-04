# Integrating DocuSign with Upward Bound

Through brainstorming ways to help make Bridget's life easier when it comes to managing Upward Bound, the idea came up potentially Embed Docusign into the site to add some automation into the way students connection with Upward Bound. There isn't a direct use case for this feature just yet, but we thought it would be useful to investigate so we could hit the ground running if Bridget has documents that need to be signed by a large number of students.  

One potential use case for the Docusign API includes having an area on the website where students and enter an email and we will use that email to send them a Docusign File to sign. The Python script could be running in the background and make the correct API call to have the signable document emailed to the student.  

# Proposed Architecture

When we come up with use cases for DocuSign in the app, we can add a feature to allow the React client to make a request to our Python server, which is where all Docusign logic will be handled. 

# DocuSign API Set up

First, download the SDK from this GitHub repository as a zip file.

This can be done by clicking the green "code" button and clicking "download as a zip file".

Next, go to the folder for Python3.7 on your machine(for my Mac, this was /Library/Python/3.7).

Finally, open the zip file in the "site packages" folder.

The easiest way to start using this module is by setting the path to this Python version an environment variable in .env

# Useful Links

Getting started with Docusign API and Authenticating API Calls
https://www.youtube.com/watch?v=SIdwJxgV5lc&t=402s

Creating an envelope(methof for sending Docusign documents via email)
https://www.youtube.com/watch?v=ev11ox1BYwk

Setting up Pythin SDK
https://developers.docusign.com/docs/esign-rest-api/sdk-tools/python/setup-and-configuration/

DocuSign REST API References and Documentation
https://developers.docusign.com/docs/esign-rest-api/reference/