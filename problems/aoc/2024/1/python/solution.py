def main():
    with open("./input", "r") as file:
        file_lines = file.readlines()

        col_1 = sorted([int(line.split("  ")[0]) for line in file_lines])
        col_2 = sorted([int(line.split("  ")[1]) for line in file_lines])

        result = 0

        for i, col_1 in enumerate(col_1):
            result += abs(col_2[i] - col_1)

        print(result)


if __name__ == "__main__":
    main()

# -- Initial solution
# def main():
#     with open("./input", "r") as file:
#         file_lines = file.readlines()
#         col_1 = []
#         col_2 = []
#
#         for line in file_lines:
#             col_1.append(int(line.split("  ")[0]))
#             col_2.append(int(line.split("  ")[1]))
#
#         sorted_col_1 = sorted(col_1)
#         sorted_col_2 = sorted(col_2)
#         result = 0
#
#         for i, col_1 in enumerate(sorted_col_1):
#             result += abs(sorted_col_2[i] - col_1)
#
#         print(result)
#
#
# if __name__ == "__main__":
#     main()
