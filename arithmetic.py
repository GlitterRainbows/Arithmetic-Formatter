def arithmetic_arranger(problems, solution=""):

  number1 = []
  operator = []
  number2 = []

  line1 = []
  line2 = []
  line3 = []
  line4 = []

  alreadydone = 0

  for elements in problems:
    problem_split = elements.split()
    number1.append(problem_split[0])
    operator.append(problem_split[1])
    number2.append(problem_split[2])

  #Too many problems error
  if len(problems) > 5:
    return "Error: Too many problems."

  if "*" in operator or "/" in operator:
    return "Error: Operator must be '+' or '-'."

  for number in number1:
    if not number.isdigit():
      return "Error: Numbers must only contain digits."
      alreadydone = 1
  for number in number2:
    if not number.isdigit() and alreadydone < 1:
      return "Error: Numbers must only contain digits."

  for digit in range(len(number1)):
    if len(number1[digit]) > 4 or len(number2[digit]) > 4:
        return "Error: Numbers cannot be more than four digits."

  #if len(number1) > len(number2):
  #  line1.append("  ")
  #  line2.append(operator, " ")
  #elif len(number2) > len(number1):
  #  line2.append("  ")

  for digit in range(len(number1)):
    if len(number1[digit]) > len(number2[digit]):
      line1.append("  " + number1[digit])
    else:
      line1.append(" "*(len(number2[digit]) - len(number1[digit]) + 2) + number1[digit])

  for digit in range(len(number2)):
    if len(number2[digit]) > len(number1[digit]):
      line2.append(operator[digit] + " " + number2[digit])
    else:
      line2.append(operator[digit] + " "*(len(number1[digit]) - len(number2[digit]) + 1) + number2[digit])

# not working
# for digit in range(len(number2)):
#  if len(number2) > len(number1):
#     line3.append("-"*(max(len(number1[digit]) + 2)))
#   else:
#      line3.append("-"*(max(len(number2[digit]) + 2)))

  for digit in range(len(number1)):
    line3.append("-"*(max(len(number1[digit]), len(number2[digit])) + 2))

  tempanswer = ""

  if solution == True:
    for digit in range(len(number1)):
      if operator[digit] == "+":
        tempanswer = str(int(number1[digit]) + int(number2[digit]))
      elif operator[digit] == "-":
        tempanswer = str(int(number1[digit]) - int(number2[digit]))

      if len(tempanswer) > max(len(number1[digit]), len(number2[digit])):
        line4.append(" " + (tempanswer))
      else:
        line4.append(" "*(max(len(number1[digit]), len(number2[digit])) - len(tempanswer) + 2) + tempanswer)

  #if tempanswer != "":
  #  arranged_problems = f"{line1}\n{line2}\n{line3}\n{line4}"
  #else:
  #  arranged_problems = f"{line1}\n{line2}\n{line3}"
    arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3) + "\n" + "    ".join(line4)
  else:
    arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
  return arranged_problems
