# fastUrlShortener
URL Shortener using FastAPI

Project Context

- On a daily basis often we have to use gigantic (and not so good-looking) URLs. Keeping the URLs short often saves space and makes it look legit. Be it in your Resume, CV or in a document, often we need to hyperlink several URLs, keeping them short and concise not only makes it look good, but also pleases the person examining them. So isn't it an amazing idea, to embed the URLs made using your own URL shortener? Yes, that's exactly what we are trying to do.

- From now use your own creation to shorten those gigantic Google App links and share it with your friends.

High-Level Approach

- Creating the FastAPI Backend and setting up folders for Templates and Static files
- Choosing our Database, setting up the models/schemas
- Implementing URL Shortening
- Implementing the mailing feature
- Linking the new and the original URL

Here's what each tool is used for:

- **Python 3.9** [download](https://www.python.org/download/) - programming the logic.
- **AstraDB** [sign up](https://dtsx.io/3nQnjz1) - highly perfomant and scalable database service by DataStax. AstraDB is a Cassandra NoSQL Database. [Cassandra](https://cassandra.apache.org/_/index.html) is used by Netflix, Discord, Apple, and many others to handle astonding amounts of data.
- **FastAPI** [docs](https://fastapi.tiangolo.com/) - as a web application framework to Display and monitor web scraping results from anywhere
