> Do not forget to create README.md with a list and explanation of your test scenarios,
why these scenarios got selected.  

# Description of testcases are in docs folder  
# Bug description example is in docs folder  
  
## Web UI test cases:  
- Minimal smoke UI tests for browsers support, and adaptive design.  
- Visual soke tests.  
- Input values cases for vulnerable fields and data range.  
- Currency values list (I doubled this case in backend tests, but I feel this place could be vulnerable).  
  
We separate logic from UI and commonly test UI functional in Web UI tests,  
so we commonly test input values and CSS issues.  
Sometimes we can test logic, but only if we think it could help to find issue earlier and do not take a lot  
of time. We could ignore cases like this, if we think it's not reasonable to spend time on it, but they  
could be useful, if we have no backend tests yet.  
  
## Backend test cases:  
- Positive smoke cases with default values.  
- Periodicity test.  
- Boundary values.  
- Some iterations with existence of input values.  
- Tricks with headers.  
- Wrong valid and invalid data.  
  
This API has no docs, so I took current state as positive and based test cases logic on it.  
I used my backend bugs experience and understanding how API works to find places with possible issues.  
All strange, possibly fail logic moments are commented or described in questions block.  
Meeting with product owner|business needed to clarify some moments.  
  
> also include additional information about used packages, your own libraries  
> and explanation why choices were made towards those libraries and assumptions you’ve made (if any).  
  
## packages used:  
- wheel - required for pytest-allure-dsl package  
- requests - the easiest and most flexible lib to make http requests  
- pytest - common core for tesing on python  
- PyHamcrest - pretty informative assertions, classic and better, than python default assertions  
- pytest-allure-dsl - allure plugin for docstring in allure, helps to keep test cases up-to-date  
- jsonschema - validate json by json-schema  
  
## custom functions:  
- ./src/antiDdosTimer - singleton object to force fixed break between requests  
- ./src/currencyHelper - func with logic to detect, how many currencies will be in result  
- ./src/datatypesHelper - func str_to_float to convert float to str with no exceptions,  
func float_zfill_tail to add as many zeros, as needed in the end of float number  
- ./src/jsonSchemaHelper - json schema validator  
- ./src/requestsHelper - http_get and make_request functions to run http request and deliver response and response code  
  
- ./tests/errors_in_formulas - validate json text formulas for correct filling  
- ./tests/random_lot - lot number generator  
  
- ./dicts/calculate - file with data lists
  
## Run tests:  
```bash  
python3 -m venv venv  
source ./venv/bin/activate  
python -m pytest -v -s --origin https://www.******.uk ./test
```  
  