> Do not forget to create README.md with a list and explanation of your test scenarios,
why these scenarios got selected.  
  
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
  