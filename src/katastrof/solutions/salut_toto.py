from threading import Condition, Thread


def alternating_salut_toto(repetitions: int) -> str:
    """Use two threads to produce `Salut Toto` repeatedly in deterministic order."""
    if repetitions <= 0:
        return ""

    condition = Condition()
    turn = {"value": "salut"}
    output: list[str] = []

    def write(word: str, my_turn: str, next_turn: str) -> None:
        for _ in range(repetitions):
            with condition:
                condition.wait_for(lambda: turn["value"] == my_turn)
                output.append(word)
                turn["value"] = next_turn
                condition.notify_all()

    salut = Thread(target=write, args=("Salut", "salut", "toto"))
    toto = Thread(target=write, args=("Toto", "toto", "salut"))
    salut.start()
    toto.start()
    salut.join()
    toto.join()
    return " ".join(output)

