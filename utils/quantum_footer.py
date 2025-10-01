import json
import os

def quantum_footer(module_name="Quantum Core"):
    manifest_path = os.path.join("components", "footer_manifest.json")
    with open(manifest_path, "r") as f:
        manifest = json.load(f)
    
    poetic_line = manifest.get(module_name, {}).get("poetic_line", "Entangle your thoughts, collapse your doubts.")
    
    footer_html = f"""
        <hr style='border: none; height: 2px; background-color: #eee;'/>
        <div style='text-align: center; font-size: 0.9rem; color: #FFD700; padding-top: 1rem;'>
            <strong>{module_name}</strong><br/>
            <em>{poetic_line}</em><br/>
            <span style='font-size: 0.8rem; color: #aaa;'>Powered by modular logic and poetic insight ⚛️</span>
        </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
