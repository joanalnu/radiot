explanation_dict = {
    'name': 'The name of the nuclide, typically including its element name and mass number.',
    'Massenzahl': 'The mass number, which is the total number of protons and neutrons in the nucleus.',
    'Ladungszahl': 'The atomic number, representing the number of protons in the nucleus, which defines the element.',
    'symbol': 'The chemical symbol for the nuclide, often including its mass number (e.g., U-235 for Uranium-235).',
    'decay_time': 'The time it takes for half of the nuclide to decay, also known as half-life.',
    'radiation_type': 'The type of radiation emitted during decay, such as alpha, beta, or gamma radiation.',
    'half_life': 'The time required for half of a sample of the nuclide to decay.',
    'stable': 'A boolean indicating whether the nuclide is stable (True) or radioactive (False).',
    'decay_modes': 'A dictionary describing the types of decay processes and their branching ratios and Q-values.',
    'abundance': 'The natural abundance of the nuclide as a fraction or percentage.',
    'Q_value': 'The energy released during a decay process, measured in MeV.'
}
notes_explanation = {
    'g': 'Gamma radiation: This indicates that the nuclide can emit gamma rays during its decay process.',
    'a': 'Alpha radiation: This indicate that the nuclide undergoes alpha decay, emitting alpha particles.',
    'b': 'Beta radiation: This indicates that the nuclide undergoes beta decay, emitting beta particles (electrons or positrons).',
    'w': "Weakly interacting: This may suggest that the nuclide's interactions with other particles or fields are minimal.",
    'm': 'Metastable state: This indicates that the nuclide is in an excited state and can transition to a lower energy state, often accompanied by gamma emission.',
    'c': 'Cosmic origin: This indicates that the nuclide may be formed through cosmic processes, such as cosmic ray interactions.',
    'r': 'Radiogenic: This indicates that the nuclide is produced through radiactive decay processes.',
    'i': 'Isomeric state: This indicates nuclides that exist in different energy states, which can affect their decay characteristics.'
}