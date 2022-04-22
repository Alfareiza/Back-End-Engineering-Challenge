![](https://github.com/Alfareiza/Back-End-Engineering-Challenge/actions/workflows/github-actions-conf.yml/badge.svg)

## Setting Up

Install Python 3.7 or later if it is not already installed. Then, set up and enter a virtual environment and run `pip install -r requirements.txt` to install the dependencies. You should then be able to run the project from the `exercise` directory by running `python manage.py runserver`.

To verify that the server is running correctly, visit `http:127.0.0.1:8000` in your browser.

## Challenge Guidelines

This Django project consists of two parts:
1. A very simple HTML page at `/connected/`.
2. A stubbed out API endpoint at `/api/converter/convert/`

Your tasks are to:
1. Add a file input to the HTML page and modify the view so that, when a file is submitted, convert it to JSON and return that to the user
2. Add the same functionality to the API endpoint, returning the converted JSON as an `application/json` response.

To test your solution, you can run `python manage.py test`. This will execute 3 tests, which attempt to submit a file and check the response.

A good solution will not only pass the tests, but also work on any user-submitted XML file.
Furthermore, a good solution should never return a 500 error and should show an error message to the user if they upload an invalid XML file.

### JSON Conversion

For the purposes of this exercise, you may ignore any XML attributes. We are only interested in converting the XML node tags and any text values into JSON.

Leaf nodes should be converted into a JSON object with the node tag as the key and the node's text value as the value. For example, `<Foo>Bar</Foo>` should be converted to `{"Foo": "Bar"}`.

Non-leaf nodes should be converted into a JSON object with the node name as the key and an array of the node's children as the value. For example:
```
<Foo>
    <Bar>Baz</Bar>
</Foo>
```
should be converted to
```javascript
{
    "Foo": [
        {"Bar": "Baz"}
    ]
}
```

The tests provide additional examples of more complex conversions.
