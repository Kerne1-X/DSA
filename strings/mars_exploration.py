def marsExploration(s: str) -> int:
    """
    Function that takes a string of SOS messages
    and returns the number of letters altered by 
    cosmic radiation.

    Example: marsExploration(SOSTOT) -> 2 

    Args:
        s (str): SOS message

    Returns:
        int: Number of letters altered by cosmic radiation during transmission
    """
    
    message = "SOS"
    count = 0
    n_sos = int(len(message))
    chunks = [s[i:i+n_sos] for i in range(0, len(s), n_sos)]
    for chunk in chunks:
        if chunk != message:
            for idx, letter in enumerate(chunk):
                if message[idx] != letter:
                    count += 1
    return count

if __name__ == "__main__":
    print(marsExploration("SOSOOSOSOSOSOSSOSOSOSOSOSOS"))
