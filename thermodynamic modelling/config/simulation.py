from dataclasses import dataclass

@dataclass
class simulationEngineParameters :
   crank_angle_step=0.25
   start_angle=0
   end_angle=720
   solver=None
   combustion_model_emperical_relation="wiebe function"
   heat_transfer_model="woschni function"


   csv_file=True
   exel_file=True
   figures=True
   result_plot=True
   validation_model=True
   export_bc_cfd=True
   ml_datasets=True
   