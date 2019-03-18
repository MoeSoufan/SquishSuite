import login, studyFunctions, short3d, biplanarLAX, ctModules, cvi42Objects, drawContours, loadStudy, report42, flowModule, flowAnalysisModule
import sys, os, subprocess, time

def for_each_call(frame, event, arg):
    snooze(0.01)
      
def init():
    sys.setprofile(for_each_call)
    
def main():
    total_start = time.time()
    attachToApplication("MyApplicationAttachable")
    
    # Login
    login.login("moeadmin", "everclear")
     
    # Anonymize study
    anon_study = studyFunctions.anonymize_study("ConcurrencyTest\\_Tester2", "Concurrency-Test1")

    # Load study
    loadStudy.load(anon_study)
    snooze(20)
    
    # Draw and send viewer module
    studyFunctions.click_module("Viewer")
    studyFunctions.load_series("viewer1", 1)
    drawContours.lineContour("viewer1", 5)
#     report42.add_to_report()
    snooze(10)
     
    # Send capture
    studyFunctions.click_module("Viewer")
    # Edit check report42
#     report42.measurement_capture()

    snooze(10)

    # Draw and send systemic flow
    studyFunctions.click_module("Flow")
    flowAnalysisModule.select_systemic()
    
    studyFunctions.load_series("flow1", 16)
    drawContours.flowContour("flow1", 1)
    flowAnalysisModule.segment_forward()
#     report42.add_to_report()
    snooze(10)
    
    # Draw and send pulmonary flow
    studyFunctions.click_module("Flow")
    flowAnalysisModule.select_pulmonary()
    studyFunctions.load_series("flow1", 17)
    drawContours.flowContour("flow1", 2)
    flowAnalysisModule.segment_forward()
#     report42.add_to_report()
    snooze(10)
    
    # Select and send comparison flow
    studyFunctions.click_module("Flow")
    flowAnalysisModule.select_comparison()
#     report42.add_to_report()
    snooze(10)
        
    # export study
    studyFunctions.close_study()
    studyFunctions.export_study(anon_study)
    studyFunctions.delete_study(anon_study)
    total_end = time.time()
     
    test.log("Total time: %.2f" % (total_end-total_start))