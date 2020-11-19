# Created by Vince at 11/17/2020
Feature: Calculating Retirement Age and Date
  As a potential retiree or an investor looking towards the future,
  users should be able to input their birth year,
  determine the retirement age, and find the date of retirement.

  Scenario Outline: Valid Birth Year Input
    Given the user enters "<year>" for the birth year
    When the "<year>" is tested for validity
    Then the program will continue to run is the "<year>" is valid

    Examples: Inputs
     | year |
     | 1900 |
     | 1930 |
     | 1936 |
     | 1937 |
     | 1938 |
     | 1939 |
     | 1940 |
     | 1941 |
     | 1942 |
     | 1943 |
     | 1948 |
     | 1954 |
     | 1955 |
     | 1956 |
     | 1957 |
     | 1958 |
     | 1959 |
     | 1960 |
     | 1964 |
     | 2020 |

  Scenario Outline: Invalid Birth Year Input
    Given the user enters "<year>" for the birth year
    When the "<year>" is tested for validity
    Then the program finds the input invalid and should return an error message for that "<year>"
    Examples:
      | year |
      | 1899 |
      | 2021 |
      | abc  |
      | True |

  Scenario Outline: Valid Birth Month Input
    Given the user puts "<month>" for the birth month
    When the "<month>" is checked if it is a valid input
    Then the program should continue to run if "<month>" is valid

    Examples:
      | month |
      | 1     |
      | 2     |
      | 3     |
      | 4     |
      | 5     |
      | 6     |
      | 7     |
      | 8     |
      | 9     |
      | 10    |
      | 11    |
      | 12    |

  Scenario Outline: Invalid Birth Month Input
    Given the user puts "<month>" for the birth month
    When the "<month>" is checked if it is a valid input
    Then the program should return an error message if "<month>" is invalid

    Examples:
      | month |
      | 0     |
      | 13    |
      | abc   |
      | True  |

  Scenario Outline: Calculate Retirement Age
    Given the user enters "<year>" for the birth year
    When the "<year>" is tested for validity
    Then the program should get the retirement age "<r_age>" and retirement month of "<r_month>" for the year "<year>"

    Examples:
     | year | r_age | r_month |
     | 1900 | 65    | 0       |
     | 1930 | 65    | 0       |
     | 1936 | 65    | 0       |
     | 1937 | 65    | 0       |
     | 1938 | 65    | 2       |
     | 1939 | 65    | 4       |
     | 1940 | 65    | 6       |
     | 1941 | 65    | 8       |
     | 1942 | 65    | 10      |
     | 1943 | 66    | 0       |
     | 1948 | 66    | 0       |
     | 1954 | 66    | 0       |
     | 1955 | 66    | 2       |
     | 1956 | 66    | 4       |
     | 1957 | 66    | 6       |
     | 1958 | 66    | 8       |
     | 1959 | 66    | 10      |
     | 1960 | 67    | 0       |
     | 1964 | 67    | 0       |
     | 2020 | 67    | 0       |


   Scenario Outline: Calculate Retirement Date
    Given the user inputs both "<year>" and "<month>"
    When both "<year>" and "<month>" return as valid
    Then the program will add "<year>" to retiring age and "<month>" to retiring month to find the "<r_date>"

    Examples:
      | year | month | r_date            |
      | 1937 | 1     | January of 2002   |
      | 1938 | 1     | March of 2003     |
      | 1939 | 2     | June of 2004      |
      | 1940 | 3     | September of 2005 |
      | 1941 | 4     | December of 2006  |
      | 1942 | 5     | March of 2008     |
      | 1943 | 6     | June of 2009      |
      | 1955 | 7     | September of 2021 |
      | 1956 | 8     | December of 2022  |
      | 1957 | 9     | March of 2024     |
      | 1958 | 10    | June of 2025      |
      | 1959 | 11    | September of 2026 |
      | 1960 | 12    | December of 2027  |
      | 1964 | 6     | June of 2031      |
