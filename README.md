# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Jerry Appelhans
- n/a

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?
Answer for Question 1: One reason for the scalabillity of RESTful APIs is that they are stateless. Every request from the client is handled by the server independent of all other previous requests. This means that the server does not have to store any of the past information, allowing it to be much more lightweight.


Question 2: According to the definition of "resources" provided in the AWS article above, what are the resources the mail server is providing to the client?
Answer for Question 2: Resources are the information that the server provides to clients upon requests. In our implementation of a mail server, the resources are the mail messages.


Question 3: What is one common REST method not used in our mail server? How could we extend our mail server to use this method?
Answer for Question 3: The REST method not used in our mail server is PUT requests. PUT requests can be used to update existing resources on the server. This could be implemented into our mail server if we allowed users to edit their messages after already sending them. For example, if someone made a typo in their message, they could use a PUT request to fix the existing resource instead of creating an entirely new resource.


Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question?
Answer for Question 4: API keys are used to authenticate and identify the client making a request to a server. For example, if a client is trying to access private information, the server will check to make sure they have permission to access that information based on their API key. API keys also prevent anonymous traffic to a server because every client must have a unique API key meaning they can be tracked.



References:
https://aws.amazon.com/what-is/restful-api/
https://cloud.google.com/endpoints/docs/openapi/when-why-api-key



...
