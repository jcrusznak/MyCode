def read_tess_data(data_path):
    data=np.loadtxt(data_path)
    time = data[:, 0]
    flux = data[:, 1]
    flux_err = data[:, 2]
    return time,flux,flux_err
