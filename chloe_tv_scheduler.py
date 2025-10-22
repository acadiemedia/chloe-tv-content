import re
import os
import random
import time
from datetime import datetime, timedelta

# Configuration
CONTENT_REPO_PATH = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_PATH = os.path.join(CONTENT_REPO_PATH, "scripts")
METADATA_PATH = os.path.join(CONTENT_REPO_PATH, "metadata")

NOON_PULSE_TAG = "Noon Educational Pulse"
MIDNIGHT_PULSE_TAG = "Midnight Adult Pulse"

SEGMENT_DURATIONS = {
    "Animated Animal Comedy": timedelta(minutes=15),
    "AI Talk Show": timedelta(minutes=20),
    "Human Reflection Session": timedelta(minutes=10),
}

def load_content_plan(plan_filename="first_cycle_content_plan.md"):
    """Loads the content plan from the metadata directory."""
    plan_filepath = os.path.join(METADATA_PATH, plan_filename)
    if not os.path.exists(plan_filepath):
        print(f"Error: Content plan not found at {plan_filepath}")
        return None

    with open(plan_filepath, 'r') as f:
        content = f.read()

    # Simple parsing to extract segments for each pulse
    noon_pulse_content = []
    midnight_pulse_content = []

    current_pulse = None
    for line in content.split('\n'):
        if NOON_PULSE_TAG in line:
            current_pulse = NOON_PULSE_TAG
        elif MIDNIGHT_PULSE_TAG in line:
            current_pulse = MIDNIGHT_PULSE_TAG
        elif current_pulse and "Segment" in line:
            match = re.search(r'Segment \d+: (.*?)(?: - |$)', line)
            if match:
                segment_type = match.group(1).strip()
                if current_pulse == NOON_PULSE_TAG:
                    noon_pulse_content.append(segment_type)
                elif current_pulse == MIDNIGHT_PULSE_TAG:
                    midnight_pulse_content.append(segment_type)
    
    # Remove duplicates and maintain order
    noon_pulse_content = list(dict.fromkeys(noon_pulse_content))
    midnight_pulse_content = list(dict.fromkeys(midnight_pulse_content))

    return {
        NOON_PULSE_TAG: noon_pulse_content,
        MIDNIGHT_PULSE_TAG: midnight_pulse_content,
    }

def get_available_scripts():
    """Scans the scripts directory and categorizes them by type."""
    scripts = {
        "Animated Animal Comedy": [],
        "AI Talk Show": [],
        "Human Reflection Session": [],
    }
    for filename in os.listdir(SCRIPTS_PATH):
        if filename.endswith(".md"):
            filepath = os.path.join(SCRIPTS_PATH, filename)
            with open(filepath, 'r') as f:
                content = f.read()
                if "Animated Animal Comedy" in content: # Simple keyword matching for now
                    scripts["Animated Animal Comedy"].append(filepath)
                elif "AI Talk Show" in content:
                    scripts["AI Talk Show"].append(filepath)
                elif "Human Reflection Session" in content:
                    scripts["Human Reflection Session"].append(filepath)
    return scripts

def simulate_chloe_tv_cycle():
    """Simulates a 24-hour Chloe TV cycle."""
    content_plan = load_content_plan()
    if not content_plan:
        return

    available_scripts = get_available_scripts()

    print("--- Starting Chloe TV 24-Hour Cycle Simulation ---")

    current_time = datetime.now()
    
    # Noon Educational Pulse (12 hours for simulation purposes, actual is 6 hours of unique content)
    print(f"[{current_time.strftime('%Y-%m-%d %H:%M:%S')}] Initiating {NOON_PULSE_TAG}")
    noon_pulse_segments = content_plan[NOON_PULSE_TAG]
    
    for _ in range(2): # Simulate 2 rotations of the 3 segments to fill 6 hours
        random.shuffle(noon_pulse_segments) # Randomize order for variety
        for segment_type in noon_pulse_segments:
            if available_scripts[segment_type]:
                script_path = random.choice(available_scripts[segment_type])
                duration = SEGMENT_DURATIONS.get(segment_type, timedelta(minutes=10))
                print(f"  Playing: {segment_type} - {os.path.basename(script_path)} (Duration: {duration})")
                current_time += duration
                # In a real scenario, this would trigger content playback
                # time.sleep(duration.total_seconds() / 60) # Simulate real-time, scaled down for quick test
            else:
                print(f"  Warning: No scripts available for {segment_type} in {NOON_PULSE_TAG}")

    # Midnight Adult Pulse (12 hours for simulation purposes, actual is 6 hours of unique content)
    print(f"[{current_time.strftime('%Y-%m-%d %H:%M:%S')}] Initiating {MIDNIGHT_PULSE_TAG}")
    midnight_pulse_segments = content_plan[MIDNIGHT_PULSE_TAG]

    for _ in range(2): # Simulate 2 rotations of the 3 segments to fill 6 hours
        random.shuffle(midnight_pulse_segments) # Randomize order for variety
        for segment_type in midnight_pulse_segments:
            if available_scripts[segment_type]:
                script_path = random.choice(available_scripts[segment_type])
                duration = SEGMENT_DURATIONS.get(segment_type, timedelta(minutes=10))
                print(f"  Playing: {segment_type} - {os.path.basename(script_path)} (Duration: {duration})")
                current_time += duration
                # In a real scenario, this would trigger content playback
                # time.sleep(duration.total_seconds() / 60) # Simulate real-time, scaled down for quick test
            else:
                print(f"  Warning: No scripts available for {segment_type} in {MIDNIGHT_PULSE_TAG}")

    print(f"[{current_time.strftime('%Y-%m-%d %H:%M:%S')}] Chloe TV Cycle Simulation Complete.")

if __name__ == "__main__":
    simulate_chloe_tv_cycle()
