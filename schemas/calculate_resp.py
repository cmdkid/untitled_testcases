scheme = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
      "commission": {
        "type": "null"
      },
      "long": {
        "type": "string"
      },
      "lots_mln_usd": {
        "type": "string"
      },
      "margin": {
        "type": "string"
      },
      "margin_formula1": {
        "type": "string",
        "enum": ["Lots x Contract size x Required margin"]
      },
      "margin_formula2": {
        "type": "string"
      },
      "no_quotes": {
        "type": "boolean"
      },
      "profit": {
        "type": "string"
      },
      "profit_formula1": {
        "type": "string",
        "enum": ["Point size x Contract size x Lots"]
      },
      "profit_formula2": {
        "type": "string"
      },
      "short": {
        "type": "string"
      },
      "swap_char": {
        "type": "string"
      },
      "swap_enable": {
        "type": "boolean"
      },
      "swap_formula1": {
        "type": "string",
        "enum": ["Lots x Contract size x Short_or_Long x Point size"]
      },
      "swap_formula2": {
        "type": "string"
      },
      "swap_formula3": {
        "type": "string"
      },
      "swap_long": {
        "type": "string"
      },
      "swap_short": {
        "type": "string"
      },
      "tick_size": {
        "type": "integer"
      },
      "user_currency": {
        "type": "string"
      },
      "volume_formula1": {
        "type": "string",
        "enum": ["Lots x Contract size"]
      },
      "volume_formula2": {
        "type": "string"
      },
      "volume_mln_usd": {
        "type": "string"
      },
      "form_type": {
        "type": "string",
        "enum": ["classic"]
      }
  },
  "required": [
    "commission",
    "conversion_pairs",
    "long",
    "lots_mln_usd",
    "margin",
    "margin_formula1",
    "margin_formula2",
    "no_quotes",
    "profit",
    "profit_formula1",
    "profit_formula2",
    "short",
    "swap_char",
    "swap_enable",
    "swap_formula1",
    "swap_formula2",
    "swap_formula3",
    "swap_long",
    "swap_short",
    "tick_size",
    "user_currency",
    "volume_formula1",
    "volume_formula2",
    "volume_mln_usd",
    "form_type"
  ]
}
