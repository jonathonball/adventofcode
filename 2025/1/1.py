from classes import Challenge

if __name__ == "__main__":
    challenge = Challenge(debug=True)
    challenge.execute()
    print(f"Final value: {challenge.safe.zero_count}")
