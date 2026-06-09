class SustainabilityEngine:
    """Calculates carbon footprint savings compared to Styrofoam."""
    
    def calculate_carbon_offset(self, weight_kg):
        # Styrofoam factor: ~3kg CO2 per 1kg of material
        # Mycelium is carbon-negative
        CO2_SAVED_PER_KG = 3.5 
        return weight_kg * CO2_SAVED_PER_KG

    def assess_integrity(self, sensor_data):
        """ML inference logic (placeholder)."""
        # Logic to flag if package is damaged based on temperature/shock data
        if sensor_data['temp'] > 40:
            return "WARNING: Structural Integrity Compromised"
        return "SAFE"