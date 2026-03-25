# API Assignment - Answers

## 1. What is the role of query parameters in this request?
Query parameters are the extra details we pass in the URL to tell the API what exactly we want.
In this request I used:
`q=python` -> to search for python related repositories
`sort=stars` -> to sort the results by number of stars
`order=desc` -> to get highest stars first
`per_page=5` -> to limit the results to only 5 repos
Without query parameters the API would not know what to search for or how to filter the results. They basically help us customize the request.
Example: `https://api.github.com/search/repositories?q=python&sort=stars&order=desc&per_page=5`

## 2. Why do we use response.json() instead of response.text?

`response.text` gives the raw response as a plain string. It looks like this:
`{"total_count":123456,"items":[{"name":"repo1"...}]}`
It is just a big string and we cannot directly access values from it like `data["items"]`.
`response.json()` converts that string into a proper Python dictionary so we can easily access the data like `data["items"]` or `repo["name"]`.
So basically `response.json()` makes it easier to work with the data in Python.