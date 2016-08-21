# currency_converter
Currency Converter homework

_This assignment was completed as part of my coursework at The Iron Yard._

Thinking with objects is a great way to understand how your code works from a high level. Let's build a program to convert and perform math on currency values!

**Objectives**

This assignment should reinforce the object oriented programming methods we covered in class and you should feel more familiar in the following after:

- Overriding Python's magic (init) methods for comparison and math.
- Writing cleaner and more readable code.
- Thinking with objects rather than primitive data types.

**Description**

There are many currencies around the world. When travelers are moving between countries they commonly have to convert their money to another currency to ensure they can buy the goods they require. However since we're dealing with money we need to make sure that our software does precisely what we say it does with 0 room for error.

**Currency Conversion**

A small example of a currency conversion is converting USD (united states dollars) to EUR (euro). To convert your dollars to euros you would want to multiply by the current euro -> usd rate. As of the time of this writing the Euro was worth 0.9 to the USD 1.0. That is the equivalent of saying "If I gave you 1 USD you would give me back 9/10th of a Euro".

**Normal Mode**

- Create a Money class that can store it's own amount and currency symbol.
- Override the methods on your Money class so that you can perform numeric operations between two instances of the money class.
- Implement >= > <= < + - == != * operator overloads.
- Implement the conversion rates for USD, JPY, EUR, and BTC.

Example:

>>> Money(100.00, "USD") + Money(56.32, "EUR")

Output the addition result in USD. The EUR must be converted for this to work!

**Hard Mode**

All of the features of normal mode in addition to the following:

Allow multiple operations and currencies to be chained together as one operation.
Example:

>>> Money(100.00, "USD") + Money(56.32, "EUR") + Money(1.2, "BTC") + Money(8, "USD")

Output the addition result in USD. All values must be converted for this to work!

**Conversion rates**

Make sure your conversion rates are as close to current as possible. Be as accurate as possible but don't stress if the value of the bitcoin drops the day after your assignment is due.

http://www.xe.com/currencyconverter/convert/

I used Python in order to complete this assignment.
