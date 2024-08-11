import csv
import tempfile


def main():
    """Dedupe rows in fortunes.csv based on fortune.
    """
    with tempfile.NamedTemporaryFile("r+", newline="") as tempf:
        writer = csv.writer(tempf)

        # Go through fortunes and dedupe rows based on fortune
        with open("fortunes.csv", "r", newline="") as rf:
            reader = csv.reader(rf)

            # Skip header
            header_row = reader.__next__()
            writer.writerow(header_row)

            fortune_set = set()
            for row in reader:
                if row[0] not in fortune_set:
                    fortune_set.add(row[0])
                    writer.writerow(row)

        # Re-wind and write to fortunes
        tempf.seek(0)
        with open("fortunes.csv", "w", newline="") as wf:
            for line in tempf:
                wf.write(line)


if __name__ == "__main__":
    main()
