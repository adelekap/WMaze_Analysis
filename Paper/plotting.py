import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from pylab import rcParams

sigUp = 1.1
sigDown = 0.95

sessionNum = '14'
directory = '/Users/adelekap/Documents/WMaze_Analysis/Paper/plots/hierarchicalSS/'+sessionNum+'Sessions/'

def plot_results(fit, fig_no, sub_no, group):
    font = {'size': 16}
    matplotlib.rc('font', **font)
    matplotlib.rc('xtick', labelsize=15)
    matplotlib.rc('ytick', labelsize=15)

    if group == 'Young':
        color = 'green'
        dcolor = '#006600'
        yv = 0.2
    else:
        color = '#9999ff'
        dcolor = 'purple'
        yv = 0.1

    if fig_no < 3 and group == 'Young':
        plt.subplot(4,4,sub_no)
    elif fig_no <3 and group == 'Old':
        plt.subplot(4,3,sub_no)

    else:
        plt.subplot(1, 1, 1)


    plt.fill_between(np.arange(fit.shape[1]), fit[0, :], fit[2, :],
                     facecolor=color, alpha=0.5)
    if group == 'Young':
        plt.plot(fit[1, :], c=dcolor, alpha=1.0, lw=3, label='Young')
    else:
        plt.plot(fit[1, :], c=dcolor, alpha=1.0, lw=3, label='Old')

        plt.axhline(0.5, color='red', linestyle='-', label='chance = 0.5')

    last_time_below_threshold = np.where(fit[0, :] < 0.5)[-1]
    if not last_time_below_threshold.any():  # always above
        learning_trial = 1
    else:
        learning_trial = last_time_below_threshold[-1] + 2  # +2 to account for zero start and above line


    plt.xlabel('Session')
    plt.ylabel('Pr(correct)')
    plt.legend(loc='lower right', prop={'size': 15})
    plt.text(300, yv, group + ' learning session  ' + str(learning_trial))
    plt.ylim(0, 1.05)
    plt.xlim(1,21)
    plt.savefig(directory+group + str(fig_no) + '.pdf')

oldData = np.asarray([[0.33847764,0.32756602,0.28992647,0.32970299,0.36158453,0.36747828,
                       0.40016062,0.38437106,0.41216515,0.46093276,0.48209586,0.48165158,
                       0.50067709,0.50948614,0.51018911,0.53487401,0.58877753,0.60521304,
                       0.63240513,0.61674495,0.62455302,0.61737649],
                      [ 0.44297553,0.42372726,0.38103132,0.41791808,0.44801158,0.45675432,
                        0.48974314,0.4719179,0.50410529,0.54852161,0.56870409,0.56859184,
                        0.58619402,0.59582561,0.59697169,0.62053529,0.67146843,0.68656442,
                        0.71290195,0.6968187,0.70387554,0.69865321],
                      [ 0.54805605,0.52537445,0.47443934,0.50768308,0.54007925,0.54490623,
                        0.57772091,0.55934911,0.5881022,0.63263718,0.65258941,0.65271673,
                        0.66973083,0.6756946,0.67916945,0.69815938,0.74496501,0.75777496,
                        0.78249583,0.76556713,0.7727789,0.76874906]])

yngData = np.asarray([[ 0.44790475,0.48501491,0.50649736,0.51575638,0.52544606,0.52579247,
                        0.57865746,0.61021666,0.56685419,0.64761427,0.68920869,0.75374207,
                        0.74661583,0.75683762,0.73487394,0.77526965,0.81101164,0.79327991,
                        0.79391167,0.84030951,0.82861311,0.82656638],
                      [ 0.54307732,0.56862246,0.58045525,0.57827764,0.58156094,0.5838124,
                        0.63289436,0.6644412,0.62574294,0.6981322,0.73855515,0.80069697,
                        0.79104598,0.80186937,0.78241368,0.81802583,0.85063028,0.83386311,
                        0.83506886,0.8762718,0.86563864,0.8661479 ],
                      [ 0.62937088,0.64870286,0.65224175, 0.6393488,0.63535014,0.63930384,
                        0.68789653,0.7182459,0.67934369,0.74601933,0.7841635,0.84278271,
                        0.83067973,0.84083783,0.82322532,0.85415108,0.88520417,0.86967151,
                        0.86906747,0.90694799,0.89587556,0.89946474]])

plot_results(np.asarray(oldData), 3, 2, 'Old')
plot_results(np.asarray(yngData), 3, 2, 'Young')
plt.savefig(directory+'OutboundPlot.pdf')
plt.show()

outboundCertainty = [0.6410,0.7732,0.8274,0.9402,0.9416,0.9784,
                     0.9912,0.9964,0.9986,0.9998,0.9998,1.0000,1.0000,1.0000]
# outboundCertainty = [0.738,0.9060,0.9576,0.8756,0.8730,0.9842,0.9972,0.9672,0.9916,0.9958,
#                      1.0000,1.0000,0.9994,0.9978,0.9998,0.9998,0.9974,0.9908,0.9998,0.9990,0.9992]
font = {'size': 17}

matplotlib.rc('font', **font)
matplotlib.rc('xtick', labelsize=15)
matplotlib.rc('ytick', labelsize=15)
plt.axhline(1.03,lw=50,color='r',alpha=0.35)
plt.plot(range(1,15),outboundCertainty, lw=3)
plt.title('Pr(Young > Old)')
plt.ylabel('Certainty')
plt.xlabel('Session')
plt.ylim(0,1.1)
plt.xlim(1,14)
plt.savefig(directory+'OutboundPrDiffBIN.pdf')
plt.show()


oldInData = np.asarray([[ 0.36952663,0.32893907,0.44441527,0.61326733,0.79838844,0.85529669,
                          0.76187958,0.83090581,0.79227258,0.815189,0.7659065,0.85563202,
                          0.83278692,0.85719124,0.90942237,0.9129398,0.92843648,0.93728305,
                          0.89066342,0.78117802,0.85571866,0.92535074],
                        [ 0.48281508,0.41843081,0.536807,0.6917711,0.85003529,0.89755636,
                          0.83676586,0.89025318,0.86022908,0.87677018,0.83822662,0.90605192,
                          0.88984116,0.90677902,0.94417778,0.94654788,0.95674739,0.96351857,
                          0.93153127,0.85242787,0.90740364,0.9568473 ],
                        [ 0.59294882,0.50976719,0.6292739,0.76054116,0.89140006,0.92906628,
                          0.89304628,0.93034811,0.91029413,0.9209678,0.89356547,0.94121296,
                          0.930104,0.9420369,0.96631742,0.96807508,0.9749759,0.97974783,
                          0.95883134,0.90397165,0.9430431,0.97613846]])

yngInData = np.asarray([[ 0.35430062,0.34581753,0.71332491,0.80583295,0.78723032,0.84081273,
                          0.85477928,0.85141088,0.84198726,0.88596983,0.90995511,0.92218595,
                          0.92691005,0.89498167,0.90097167,0.92634759,0.91226496,0.94241541,
                          0.93704155,0.92787754,0.93983683,0.95510289],
                        [ 0.49204965,0.46302164,0.80738545,0.87608266,0.86094097,0.89991564,
                          0.89456753,0.89350968,0.88498035,0.92121679,0.93833873,0.94884595,
                          0.9523738,0.93018868,0.93275478,0.95147847,0.94269045,0.9646059,
                          0.95990625,0.95413161,0.96255347,0.97454012],
                        [ 0.62585704,0.58642642,0.8787283,0.92473034,0.91206899,0.93997204,
                          0.92649334,0.92572617,0.91804476,0.94660894,0.96025946,0.9672319,
                          0.97019539,0.95406022,0.95614345,0.9701713,0.96362334,0.97926266,
                          0.97522859,0.97189215,0.97733545,0.98708559]])

plot_results(np.asarray(oldInData), 3, 2, 'Old')
plot_results(np.asarray(yngInData), 3, 2, 'Young')
plt.savefig(directory+'InboundPlot.pdf')
plt.show()

font = {'size': 17}
inboundCertainty = [0.9998,1.0000,1.0000,0.9676,0.8688,0.7052,0.8320,
                    0.7280,0.1528,0.0256,0.0042,0.0252,0.0808,0.2692]
#
# inboundCertainty = [0.4,0.9,0.9034,0.9124,0.6758,0.7202,0.5344,0.7242,0.7016,0.6964,
#                     0.6410,0.6858,0.7894,0.3272,0.5912,0.2510,0.5228,0.9032,0.9986,0.9830,0.8536]
matplotlib.rc('font', **font)
matplotlib.rc('xtick', labelsize=15)
matplotlib.rc('ytick', labelsize=15)
plt.axhline(1.03,lw=50,color='r',alpha=0.35)
plt.plot(range(1,15),inboundCertainty, lw=3)
plt.title('Pr(Young > Old)')
plt.ylabel('Certainty')
plt.xlabel('Session')
plt.ylim(0,1.1)
plt.xlim(1,14)
plt.savefig(directory+'InboundPrDiffBIN.pdf')
plt.show()