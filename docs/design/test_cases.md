# Test Cases and Scenarios

| ID | Scenario | Expected result |
|---|---|---|
| TC01 | Full Stack aliases: JS, React.js, NodeJS, Postgres, Git | Full Stack accepted |
| TC02 | ML aliases: Python, Pandas, Scikit-learn, TensorFlow, PostgreSQL, Git | ML Engineer accepted |
| TC03 | Backend required set | Backend Developer accepted |
| TC04 | Data Scientist required set | Data Scientist accepted |
| TC05 | Missing one required qualification | Relevant profile rejected |
| TC06 | Extra qualification such as Docker | Profile can still be accepted |
| TC07 | Unknown qualification | Ignored by normalization/classification |
| TC08 | Missing email | Candidate remains parseable; email is `None` |
| TC09 | Valid DSL generated | textX accepts model |
| TC10 | Invalid DSL syntax | textX rejects model |

## Acceptance principle

A profile DFA advances when the next required canonical token is encountered. Other recognized tokens behave as self-loops. Therefore extra qualifications do not invalidate an otherwise accepted profile pattern.
