def extract_voice_summary(log_text):
    """
    Searches for the special VOICE_SUMMARY tag in the agent's output.
    """
    if not log_text:
        return "Task completed."

    lines = log_text.split('\n')
    
    # 1. Look for our explicit tag
    for line in lines:
        if "VOICE_SUMMARY:" in line:
            # return everything after the colon
            return line.split("VOICE_SUMMARY:", 1)[1].strip()
            
    # 2. Fallback: If the LLM forgot the tag, check for visual cues
    summary_buffer = []
    capture = False
    for line in lines:
        if "I can see" in line:
            capture = True
        if "Task completed" in line:
            capture = False
        if capture:
            summary_buffer.append(line)
            
    if summary_buffer:
        return "\n".join(summary_buffer)

    return "Task completed."