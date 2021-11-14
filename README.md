# Fallas2-TP

## HOW-TO

1. Navigate to the proyect
2. Run `docker compose up --build`
3. App is running locally on `localhost:5000`

## Example

`POST` commando to `localhost:5000/evaluate` with the following JSON body:
```
{
    "season": 3,
    "temperature": 1,
    "water state": 2,
    "fishing depth": 2,
    "time": 5,
    "fish size": 3,
    "bait": 1,
    "has telescopic rod": true,
    "reel size": 1,
    "has reel stop": false,
    "line diameter": 1,
    "has plumb": true,
    "plumb weight": 1
}
```

The response should look like this:
````
{
    "suggestion": "Pejerrey"
}
