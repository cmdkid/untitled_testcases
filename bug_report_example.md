##### note:  
This bug is a fake, just to show bug report  
  
## Environment:  
- Desktop  
- OS X 10.15.6  
- Firefox 81.0.1 (64-bit)  
- Screen resolution: 1680 × 1050  
- IP in Norway region  
  
## Iterate steps:  
- Open [link](https://www.******.uk/tools/calculator/)  
- Set input values:  
  - "Forex" = CADJPY  
  - "Account currency" = MAGUSD  
  - "Lot" = 0.955  
- Click "Calculate"  
  
## Expected result:  
In block "Point profit", value "Volume" is "0.01000 x 100000.0 x 0.95 = 955.00 JPY".  
  
## Actual result:  
In block "Point profit", value "Volume" is "0.01000 x 100000.0 x 0.96 = 960.00 JPY".  
  
Backend request url: https://www.exness.uk/api/calculator/calculate/?form_type=classic&instrument=Forex&symbol=CADJPY&lot=0.955&leverage=200&user_currency=MAG  
response:  
```json  
{  
  "commission": null,  
  "conversion_pairs": {  
    "USDCAD": 1.3262,  
    "MAGUSD": 0.60864,  
    "USDJPY": 105.609  
  },  
  "long": "-0.63",  
  "lots_mln_usd": "0.17",  
  "margin": "3904.35",  
  "margin_formula1": "Lots x Contract size x Required margin",  
  "margin_formula2": "0.95 x 100000.0 x 3.3% = 3151.503 CAD",  
  "no_quotes": false,  
  "profit": "14.86",  
  "profit_formula1": "Point size x Contract size x Lots",  
  "profit_formula2": "0.01000 x 100000.0 x 0.96 = 960.00 JPY",  
  "short": "-2.42",  
  "swap_char": "pt.",  
  "swap_enable": true,  
  "swap_formula1": "Lots x Contract size x Short_or_Long x Point size",  
  "swap_formula2": "0.95 x 100000.0 x -0.04210 x 0.01000 = -40.21 JPY",  
  "swap_formula3": "0.95 x 100000.0 x -0.16290 x 0.01000 = -155.57 JPY",  
  "swap_long": "-0.04",  
  "swap_short": "-0.16",  
  "tick_size": 0,  
  "user_currency": "MAG",  
  "volume_formula1": "Lots x Contract size",  
  "volume_formula2": "0.95 x 100000 = 95500.00 CAD",  
  "volume_mln_usd": "0.0720",  
  "form_type": "classic"  
}  
```  
  
### Possible causes:  
Wrong round method for lot in backend logic.  
