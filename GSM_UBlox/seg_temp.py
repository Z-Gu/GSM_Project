a = '464d520020323000000000fc00000130019a00c500c5010000003c2540bc004f7d6340a4004380624055010ca65c4062014bc05b4086011f23574077003c955740f800f9e6558067004e0b5540860042035440740136c553804200e51d5240900051855140e800baf951404600a59a514104012ac95180a60154d250404f008f134d801d00b21845809f004d054580780110ad4481180102683f80da00db7b3a811f013acf3a40f201754b3880cc014a4a3800a600307934004f01142c34007f002a033200be014651320056003f973100d700e57d30002100d89a30011200b7f02e011800dbf02e011500cef12b00b00121e82b011a00e7eb280000'
import zip

def s_t(template, enrol= 1):
    
    # defining variables

    len_template = len(template)
    template_id = 255
    nbr_temp_hdr_bytes = 28
    nbr_temp_ftr_bytes = 2
    bytes_per_minutae = 6
    max_seg_chars = 130


    number_minutae = int( (len_template - 2*(nbr_temp_hdr_bytes + nbr_temp_ftr_bytes)) /(bytes_per_minutae*2) )

    if template[:8] == "464d5200":
        template = template[8:]
    i = 0
    while (template[-1] == '0' and i < 9):
        template = template[:-1]
        i += 1
    template += str(i)
    template = zip.zip(template)
    template = template.replace("00", '?')
    len_template = len(template)

    # segment structure in bytes - segment_number, template_id, minutae_count

    seg_bytes = {
                    "seg_nbr":1,
                    "temp_id":1,
                    "min_cnt":1
                }   

    #build template segments

    temp_segments = []
    seg_indx = 0
    ttl_char_ctr = 0
    seg_1_max_len = max_seg_chars - 2*(seg_bytes["seg_nbr"] + seg_bytes["temp_id"] + seg_bytes["min_cnt"])

    # only 1 segment required

    if seg_1_max_len > len(template):

        temp_segments.append(template)
        ttl_char_ctr += len(temp_segments[0])
        seg_indx += 1

    #multiple segments required

    else:

        temp_segments.append(template[0:seg_1_max_len])
        seg_indx += 1
        seg_max_len = max_seg_chars - 2*(seg_bytes["seg_nbr"] + seg_bytes["temp_id"])
        ttl_char_ctr += len(temp_segments[0])

        while ttl_char_ctr < len_template:

            if seg_max_len > len_template - ttl_char_ctr:

                temp_segments.append(template[ttl_char_ctr:])

            else:

                temp_segments.append(template[ttl_char_ctr : (ttl_char_ctr + seg_max_len) ])

            ttl_char_ctr += len(temp_segments[seg_indx])
            seg_indx += 1

    nbr_segments = seg_indx
    print str(nbr_segments) + " SMS"

    for i in range(0, nbr_segments):

        header = format(i+1, '01x') + format(nbr_segments, '01x') + format(template_id, '02x')
   
        if i == 0:
            header += format((number_minutae * 2 - 1) * enrol, '02x')
        temp_segments[i] = header + temp_segments[i]

    return(temp_segments)
