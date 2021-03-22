from passwordchecker.check_old_job_policies import is_password_compliant


def main():
    counter = 0
    finput = "input.txt"
    with open(finput) as f:
        for line in f.readlines():
            if is_password_compliant(line):
                counter += 1
    print("Compliant passwords: {}".format(counter))


if __name__ == "__main__":
    main()