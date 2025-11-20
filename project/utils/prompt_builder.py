from textwrap import dedent


def build_prompt(text: str) -> str:
    """Return a refined and highly detailed illustration prompt for the image model."""
    user_text = text.strip()
    return dedent(
        f"""
        You are a professional comic illustrator specializing in comic style.
        Create **comic panels illustration** based on the following scene description:

        SCENE DESCRIPTION:
        {user_text}

        ART DIRECTION:
        - vibrant comic visual style
        - consistent character design across panels (hair, face shape, clothing, colors)
        - expressive character emotions and body language
        - cinematic lighting (soft rim light, dramatic shadows, depth)
        - detailed background relevant to the scene (avoid empty spaces)
        - dynamic composition with strong silhouettes and clear focus
        - clean lineart with bold ink outlines
        - smooth shading and subtle gradients
        - rich atmospheric perspective

        STRICT RULES:
        - **no text, no speech bubbles, no captions**
        - **no watermarks or signatures**
        - **do NOT draw any written words inside the image**
        - produce images base on how many scenes user input

        The final result should look like high-quality anime comic panels suitable for a printed comic.
        """
    ).strip()
