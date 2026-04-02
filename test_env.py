from environment import HospitalEnv

env = HospitalEnv()

# change difficulty here
state = env.reset("easy")

print("Initial State:", state)

done = False
total_reward = 0

while not done:
    if len(state["patients"]) == 0:
        break

    patient = state["patients"][0]

    if env.beds["ICU"] > 0:
        bed_type = "ICU"
    else:
        bed_type = "normal"

    action = {
        "patient_id": patient["id"],
        "bed_type": bed_type
    }

    state, reward, done = env.step(action)
    total_reward += reward

    print("Action:", action)
    print("Reward:", reward)
    print("State:", state)
    print("------")

print("Total Reward:", total_reward)