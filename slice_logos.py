from PIL import Image

def slice_image():
    try:
        img = Image.open('marcas.png')
    except Exception as e:
        print("Erro ao abrir imagem:", e)
        return

    w, h = img.size
    cols = 4
    rows = 4
    tile_w = w // cols
    tile_h = h // rows

    count = 1
    for r in range(rows):
        for c in range(cols):
            left = c * tile_w
            top = r * tile_h
            right = left + tile_w
            bottom = top + tile_h
            
            crop = img.crop((left, top, right, bottom))
            crop.save(f'logo_crop_{count}.png')
            count += 1
            
    print(f"Dividido com sucesso em {count-1} logos")

slice_image()
