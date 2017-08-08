# Zomatopy
A Python wrapper for the Zomato API v2.1

## Installation

    pip install zomatopy
(Not yet uploaded to Pypi - will not work)

## Getting Started
### Python Version
This wrapper was written for Python 3 and might not work well with Python 2.

### Adding Zomatopy to your application
For use with only user based authentication we can create the following configuration:

```python
import zomatopy

config={
  "user_key"="ZOMATO_API_KEY"
}
    
zomato = zomatopy.initialize_app(config)
```
