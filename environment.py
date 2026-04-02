import random

class HospitalEnv:

    def __init__(self):
        self.beds = {}
        self.patients = []
        self.done = False

    def reset(self, difficulty="easy"):

        if difficulty == "easy":
            self.beds = {"ICU": 2, "normal": 3}
            num_patients = 3

        elif difficulty == "medium":
            self.beds = {"ICU": 2, "normal": 2}
            num_patients = 5

        elif difficulty == "hard":
            self.beds = {"ICU": 1, "normal": 2}
            num_patients = 8

        else:
            raise ValueError("Invalid difficulty")

        self.patients = [
            {"id": i, "severity": random.choice(["high", "low"])}
            for i in range(num_patients)
        ]

        self.done = False
        return self.state()

    def state(self):
        return {
            "beds": self.beds,
            "patients": self.patients
        }

    def step(self, action):

        if self.done:
            return self.state(), 0, True

        reward = 0

        patient = next((p for p in self.patients if p["id"] == action["patient_id"]), None)

        if patient is None:
            reward = -1
        elif action["bed_type"] not in self.beds:
            reward = -1
        elif self.beds[action["bed_type"]] <= 0:
            reward = -1
        else:
            self.beds[action["bed_type"]] -= 1
            self.patients.remove(patient)

            if patient["severity"] == "high" and action["bed_type"] == "ICU":
                reward = 2
            elif patient["severity"] == "low" and action["bed_type"] == "normal":
                reward = 1
            else:
                reward = -0.5

        if len(self.patients) == 0:
            self.done = True

        return self.state(), reward, self.done


# ✅ MAIN EXECUTION BLOCK (FIX)
if __name__ == "__main__":
    env = HospitalEnv()

    print("Resetting environment...\n")
    state = env.reset("easy")
    print("Initial State:", state)

    # Loop until all patients are assigned
    while not env.done:

        if len(env.patients) == 0:
            break

        # Select first patient
        patient = env.patients[0]
        patient_id = patient["id"]

        # Simple decision logic
        if patient["severity"] == "high":
            bed_type = "ICU"
        else:
            bed_type = "normal"

        action = {
            "patient_id": patient_id,
            "bed_type": bed_type
        }

        next_state, reward, done = env.step(action)

        print("\nAction:", action)
        print("Reward:", reward)
        print("Next State:", next_state)
        print("Done:", done)