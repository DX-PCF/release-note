
# Title: September 25, 2025 
Link: https://cloud.google.com/release-notes#September_25_2025<br>
## Cloud Service Mesh
### Deprecated
原文: Support for the following features will end on **March 17, 2027**:
- GKE on AWS
- GKE on Azure
- EKS Attached Clusters on AWS
- Azure Attached Clusters with AKS

[GKE on AWS](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement)
[GKE on Azure](https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement)
 Note that there are no changes to the other features of GKE attached clusters or Google Distributed Cloud (software only or air-gapped),
 You must migrate to an alternative service mesh solution or an alternative Istio-based solution using your existing CSM configuration files by March 17, 2027.

説明:
Cloud Service Mesh (CSM) における、以下のマルチクラウドおよびアタッチドクラスター環境のサポートが、**2027年3月17日**をもって終了します。

*   GKE on AWS
*   GKE on Azure
*   EKS Attached Clusters on AWS
*   Azure Attached Clusters with AKS

これは、GKEアタッチドクラスターの他の機能や、Google Distributed Cloud (ソフトウェアのみまたはエアギャップ環境) には影響しません。対象となる環境でCloud Service Meshを利用している場合、指定された期日までに、代替のサービスメッシュソリューションまたは既存のCSM構成ファイルを利用したIstioベースのソリューションへの移行が必要です。

影響有無:
影響なし。
理由: 貴社環境で利用されているのはGoogle Cloud Composer2であり、GKE on AWS, GKE on Azure, EKS Attached Clusters on AWS, Azure Attached Clusters with AKS のいずれも直接利用していないため、この廃止予定の対象外です。

対処方法:
特になし。

用語説明:
*   **Cloud Service Mesh (CSM):** Google Cloudが提供する、マイクロサービス間の通信管理、トラフィック制御、ポリシー適用、可観測性などを実現するためのサービスメッシュソリューション。Anthos Service Meshに統合されています。
*   **GKE on AWS / GKE on Azure:** Google Kubernetes EngineをGoogle Cloud以外のインフラストラクチャ（AWSまたはAzure）上で実行するためのGoogle Cloudのサービス。マルチクラウド環境でのKubernetes管理を可能にします。
*   **Attached Clusters (EKS Attached Clusters / Azure Attached Clusters with AKS):** 既存のAWS EKSクラスターやAzure AKSクラスターをGoogle Cloudに登録し、AnthosサービスメッシュやGoogle Cloudの管理機能の一部を利用できるようにする機能。

---

## Google Kubernetes Engine
### Issue
原文: **Issue with A4X machine type compatibility on certain GKE versions**
 Certain GKE versions are not compatible with the A4X machine type. The issue is that a Container-Optimized OS (COS) image that these GKE versions depend on was not built as a multi-architecture image. This incompatibility causes an `exec format` error on the Arm-based A4X machines. The issue affects GKE versions 1.33.2-gke.1377000 or later, and any versions earlier than 1.33.4-gke.1036000.

説明:
特定のGKEバージョンにおいて、A4Xマシンタイプ（Armベース）との互換性問題が確認されています。この問題は、該当するGKEバージョンが依存するContainer-Optimized OS (COS) イメージが、マルチアーキテクチャ対応でビルドされていないことに起因します。結果として、ArmベースのA4Xマシンで「`exec format` error」が発生します。
この問題の影響を受けるGKEバージョンは、**1.33.2-gke.1377000以降、かつ1.33.4-gke.1036000未満**のバージョンです。

影響有無:
影響は限定的であると推測されます。
理由: 貴社環境で利用されているのはGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3)であり、通常はx86ベースのGKEノードが利用されます。A4XマシンタイプはArmベースのGPUインスタンスであり、Composerの一般的なワークロードでは直接使用されることは稀です。しかし、もしComposer環境内でGKEクラスターをカスタマイズしてA4Xマシンタイプを使用している場合、または将来的に特定のGKEバージョンがこの問題の影響を受けるCOSイメージを使用し、かつArmベースのノードが割り当てられる可能性がある場合には、影響を受ける可能性があります。

対処方法:
*   現在、GKEクラスターでA4Xマシンタイプを使用している、または今後使用する計画がある場合は、影響を受けるGKEバージョン（1.33.2-gke.1377000以降かつ1.33.4-gke.1036000未満）の使用を避け、**1.33.4-gke.1036000以上の互換性のあるバージョン**にアップグレードすることを推奨します。
*   既存のComposer環境でA4Xマシンタイプが使用されていないことを確認してください。もし不明な点があれば、Google Cloudサポートに問い合わせて、Composerが利用するGKEの基盤ノードタイプとバージョンについて確認を依頼してください。

用語説明:
*   **A4X マシンタイプ:** NVIDIA H100 GPUを搭載した、ArmベースのCPUアーキテクチャを持つGoogle CloudのVMマシンタイプです。主に高性能な機械学習やHPCワークロードに利用されます。
*   **Container-Optimized OS (COS):** Googleが提供する、コンテナ化されたワークロードの実行に特化したOSです。セキュリティ、信頼性、スピードを重視し、最小限のコンポーネントで構成されています。
*   **マルチアーキテクチャ (Multi-architecture) イメージ:** 複数の異なるCPUアーキテクチャ（例: x86-64とArm）で実行可能なようにビルドされたコンテナイメージです。
*   **exec format error:** プログラムの実行時に発生するエラーの一種で、実行しようとしているバイナリファイルが現在のCPUアーキテクチャまたはOSの実行形式と互換性がない場合に表示されます。