file_load = open("input4.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = file_in.split("\n\n")

def run():

  def valid(input_in):
    valid_count = 0
    valid_field = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for temp_pass in input_in:
      if all(temp_test in temp_pass for temp_test in valid_field):
        valid_count += 1
    return valid_count

  def verify(field_in):
    var_int = field_in[4:]
    if field_in[:3] == "byr":
      var_int = int(var_int)
      if var_int >= 1920 and var_int <= 2002:
        return True
    elif field_in[:3] == "iyr":
      var_int = int(var_int)
      if var_int >= 2010 and var_int <= 2020:
        return True
    elif field_in[:3] == "eyr":
      var_int = int(var_int)
      if var_int >= 2020 and var_int <= 2030:
        return True
    elif field_in[:3] == "hgt":
      if field_in[-2:] in ["cm", "in"]:
        var_hgt = int(field_in[4:-2])
        if field_in[-2:] == "cm":
          if var_hgt >= 150 and var_hgt <= 193:
            return True
        elif field_in[-2:] == "in":
          if var_hgt >= 59 and var_hgt <= 76:
            return True
    elif field_in[:3] == "hcl":
      if field_in[4] == "#":
        var_hcl = field_in[5:]
        if all(temp_char.isdigit() or temp_char.islower() for temp_char in var_hcl):
          return True
    elif field_in[:3] == "ecl":
      if field_in[4:] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    elif field_in[:3] == "pid":
      if len(field_in[4:]) == 9:
        return True
    elif field_in[:3] == "cid":
      return True
    return False

  def spec(input_in):
    valid_count = 0
    valid_field = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for temp_pass in input_in:
      if all(temp_test in temp_pass for temp_test in valid_field):
        temp_clean = temp_pass.replace("\n", " ").split(" ")
        if all(verify(temp_check) for temp_check in temp_clean):
          valid_count += 1
    return valid_count

  return valid(file_in), spec(file_in)