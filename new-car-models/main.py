from openai import OpenAI
from settings import settings

# Step 1: Mock Input Data
task_descriptions = [
    "Install the battery module in the rear compartment, connect to the high-voltage harness, and verify torque on fasteners.",
    "Calibrate the ADAS (Advanced Driver Assistance Systems) radar sensors on the front bumper using factory alignment targets.",
    "Apply anti-corrosion sealant to all exposed welds on the door panels before painting.",
    "Perform leak test on coolant system after radiator installation. Record pressure readings and verify against specifications.",
    "Program the infotainment ECU with the latest software package and validate connectivity with dashboard display."
]

# Step 2: Initialize Settings
config = settings()
config.load_from_env()

# Step 3: Initialize OpenAI Client
client = OpenAI(
    api_key=config.openai_api_key,
)

def generate_instruction(task_description):
    user_prompt = f"""
    You are an expert automotive manufacturing supervisor. Generate step-by-step
    work instructions for the following new model task. Include safety
    precautions, required tools (if any), and acceptance checks. Write in clear,
    numbered steps suitable for production workers.

    Task: {task_description}

    Work Instructions:
    """
    # Call OpenAI API to generate instructions
    # Using the specified model and settings
    response = client.chat.completions.create(
        model=config.openai_model,
        messages=[
            {
                "role": "system",
                "content": "You are an expert automotive technician. Provide detailed assembly instructions."
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

# Step 4: Generate and Print Instructions
for task in task_descriptions:
    instruction = generate_instruction(task)
    print(f"Task: {task}\nWork Instructions:\n{instruction}\n")