from environment import HospitalEnv


def choose_action(env, state):
    patients = state["patients"]

    # Sort: high severity first
    patients = sorted(patients, key=lambda p: p["severity"] == "low")

    patient = patients[0]

    # Always assign (NEVER return None)
    if patient["severity"] == "high":
        bed_type = "ICU" if env.beds["ICU"] > 0 else "normal"
    else:
        bed_type = "normal" if env.beds["normal"] > 0 else "ICU"

    return {
        "patient_id": patient["id"],
        "bed_type": bed_type
    }


def run_task(difficulty):
    env = HospitalEnv()
    state = env.reset(difficulty)

    total_reward = 0
    done = False

    # IMPORTANT: no premature break, always step properly
    for _ in range(50):
        if done:
            break

        # If no patients, just continue safely
        if not state.get("patients"):
            break

        action = choose_action(env, state)

        # MUST always call step with valid action
        state, reward, done = env.step(action)

        total_reward += reward

    # Normalize score
    max_reward = 20
    score = total_reward / max_reward

    return max(0.0, min(1.0, score))


if __name__ == "__main__":
    print("Running all tasks...")

    print("easy:", run_task("easy"))
    print("medium:", run_task("medium"))
    print("hard:", run_task("hard"))