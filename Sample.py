from RSDatacube.RSdc import *


if __name__ == '__main__':

    # inundated_dc = Sentinel2_dc('G:\\A_veg\\S2_all\\Sentinel2_L2A_Output\\Sentinel2_MYZR_FP_2020_datacube\\MNDWI_sequenced_datacube\\')
    # rs_dc = RS_dcs(inundated_dc)
    # rs_dc.inundation_detection('static_wi_thr', 'MNDWI', 'Sentinel2')

    inundated_dc = Sentinel2_dc('G:\\A_veg\S2_all\\Sentinel2_L2A_Output\\Sentinel2_MYZR_FP_2020_datacube\\inundation_static_wi_thr_datacube\\')
    rs_dc = RS_dcs(inundated_dc)
    water_level = pd.read_excel('G:\A_veg\Water_level\Processed\\14_螺山站_2002_2020.xlsx')
    water_level = np.array(water_level[['Date', 'water_level(m)']])
    issue_date = list(pd.read_excel('G:\\A_veg\\S2_all\\Sentinel2_L2A_Output\\Sentinel2_MYZR_FP_2020_inunduration\\cloud_issue_image\\chenghan.xlsx'))
    rs_dc.est_inunduration('inundation_static_wi_thr', 'G:\A_veg\S2_all\Sentinel2_L2A_Output\Sentinel2_MYZR_FP_2020_inunduration', water_level, process_extent=(0, 14482, 18320, 30633), manual_remove_date=issue_date)
    a = 1
