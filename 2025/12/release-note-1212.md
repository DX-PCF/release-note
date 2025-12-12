
# Title: December 10, 2025 
Link: https://docs.cloud.google.com/release-notes#December_10_2025<br>
はい、承知いたしました。Google Cloudのリリースノートを元に、構築済みのサービス（Google Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) を含む）への影響を調査し、以下のフォーマットでご回答いたします。

---

# Apigee X
## Announcement
原文: On December 10th, 2025, we released an updated version of Apigee (1-16-0-apigee-6).

 > **Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

説明: Apigee Xの新しいバージョン `1-16-0-apigee-6` がリリースされたことを知らせるアナウンスです。このバージョンは順次Google Cloudの全ゾーンに展開されるため、すべてのインスタンスに適用されるまでに数日かかる可能性があります。
影響有無: **影響なし**。Apigee Xはマネージドサービスであり、基盤のバージョンアップはGoogle Cloud側で自動的に行われます。ユーザー側での直接的な操作や設定変更は不要です。新機能や修正が適用されるまでにタイムラグがある可能性があります。
対処方法: 特になし。自動的にバージョンアップが適用されるのを待機してください。
用語説明:
*   **Apigee X**: Google Cloudが提供するAPI管理プラットフォームで、APIの設計、セキュリティ、デプロイ、モニタリングなどを一元的に行います。
*   **Rollout**: ソフトウェアや機能がユーザーやリージョンに段階的に展開されるプロセスを指します。

## Fixed
原文:
| Bug ID | Description |
| --- | --- |
| **458417250** | **Multiple authorization headers** Fixed issue where adding multiple authorization headers would cause Apigee to return a `500` error. |
| **N/A** | **Updates to security, infrastructure, and libraries.** |

説明:
*   複数のAuthorizationヘッダーがリクエストに含まれる場合に、ApigeeがHTTP 500エラーを返す不具合が修正されました。
*   セキュリティ、インフラストラクチャ、およびライブラリに関する一般的な更新が行われました。
影響有無: **影響あり（ポジティブな影響）**。
*   `458417250`: 複数のAuthorizationヘッダーを送信するAPIリクエストにおいて、これまで500エラーが発生していたケースがある場合、この修正により問題が解決され、APIの安定性が向上します。
*   `N/A`: 基盤となるセキュリティ、インフラストラクチャ、ライブラリの更新は、Apigeeサービスの全体的な堅牢性、セキュリティ体制、およびパフォーマンスの向上に寄与します。
対処方法: 特になし。これらの修正は自動的に適用され、ユーザー側で何か対処する必要はありません。
用語説明:
*   **Authorization header**: HTTPリクエストヘッダーの一つで、クライアントがサーバーに認証情報（例: アクセストークン）を送信するために使用します。
*   **HTTP 500 error**: サーバー内部で予期せぬエラーが発生したことを示すHTTPステータスコードです。
*   **Infrastructure**: システムやサービスを稼働させるための基盤となるハードウェア、ソフトウェア、ネットワークなどの構成要素です。
*   **Libraries**: ソフトウェア開発において再利用可能なコードの集合体で、特定の機能やタスクを実行するための関数やクラスが含まれます。

---

# Google Kubernetes Engine

## Changed
原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available in the Extended channel:
    - 1.28.15-gke.3188000
    - 1.28.15-gke.3225000
    - 1.29.15-gke.2505000
    - 1.29.15-gke.2553000
    - 1.30.14-gke.1746000
    - 1.30.14-gke.1794000
    - 1.31.14-gke.1033000
    - 1.32.9-gke.1575000
    - 1.33.5-gke.1862000
    - 1.34.1-gke.3355002

- The following versions are no longer available in the Extended channel:
    - 1.28.15-gke.3096000
    - 1.28.15-gke.3202000
    - 1.29.15-gke.2380000
    - 1.29.15-gke.2520000
    - 1.30.14-gke.1658000
    - 1.30.14-gke.1760000
    - 1.31.13-gke.1454000
    - 1.32.9-gke.1548000
    - 1.33.5-gke.1791000

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
    - 1.27 to 1.28.15-gke.3163000
    - 1.28 to 1.29.15-gke.2467000
    - 1.29 to 1.30.14-gke.1719000

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
    - 1.28 to 1.28.15-gke.3163000
    - 1.29 to 1.29.15-gke.2467000
    - 1.30 to 1.30.14-gke.1719000

[1.28.15-gke.3188000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.28.15-gke.3225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.2505000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.29.15-gke.2553000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1746000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[1.30.14-gke.1794000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[1.31.14-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
[1.33.5-gke.1862000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
[1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
[maintenance exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions)
[1.28.15-gke.3163000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.2467000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1719000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)

説明: GKEのExtendedチャネルにおいて、利用可能な新しいバージョンが追加され、一部の古いバージョンが利用不可になりました。また、既存のクラスタが自動的にアップグレードされる際のターゲットとなるバージョンも更新されました。これにはマイナーバージョンアップとパッチバージョンアップの両方が含まれます。
影響有無: **影響なし**。Google Cloud Composerはマネージドサービスであり、通常、その基盤となるGKEクラスタはGoogleによって管理されます。ComposerがExtendedチャネルを利用している可能性は低いですが、仮に利用していたとしても、GKEのバージョンアップグレードはGoogleが互換性を考慮して実施します。ユーザー側で直接GKEのバージョンを変更する操作は発生しません。
対処方法: 特になし。
用語説明:
*   **GKE (Google Kubernetes Engine)**: Google Cloudが提供するマネージドなKubernetesサービスです。
*   **Extended channel**: GKEのリリースチャネルの一つで、最も更新頻度が低く、長期間にわたる安定性を重視する環境向けです。
*   **Auto-upgrade targets**: GKEがクラスタのコントロールプレーンやノードを自動的にアップグレードする際の目標となるバージョンです。
*   **Maintenance exclusions**: GKEのメンテナンスウィンドウ外にアップグレードを実施しないよう設定する除外期間です。

## Changed
原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- The following versions are now available:
    - 1.31.14-gke.1033000
    - 1.31.14-gke.1081000
    - 1.32.9-gke.1575000
    - 1.32.9-gke.1632000
    - 1.33.5-gke.1956000
    - 1.34.1-gke.3355002
    - 1.34.1-gke.3403002
    - 1.34.1-gke.3556000

- The following node versions are now available:
    - 1.28.15-gke.3225000
    - 1.29.15-gke.2553000
    - 1.30.14-gke.1794000
    - 1.31.14-gke.1081000
    - 1.32.9-gke.1632000
    - 1.33.5-gke.1956000
    - 1.34.1-gke.3355002
    - 1.34.1-gke.3403002
    - 1.34.1-gke.3556000

- The following versions are no longer available:
    - 1.31.13-gke.1231000
    - 1.31.13-gke.1377000
    - 1.32.9-gke.1330000
    - 1.32.9-gke.1462000
    - 1.33.5-gke.1791000
    - 1.34.1-gke.2037001
    - 1.34.1-gke.3403001

[1.31.14-gke.1033000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.31.14-gke.1081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1575000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
[1.32.9-gke.1632000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
[1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
[1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
[1.34.1-gke.3403002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
[1.34.1-gke.3556000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
[1.28.15-gke.3225000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md#v12815)
[1.29.15-gke.2553000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#v12915)
[1.30.14-gke.1794000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md#v13014)
[1.31.14-gke.1081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1632000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
[1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
[1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
[1.34.1-gke.3403002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
[1.34.1-gke.3556000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)

説明: GKEの全般的なバージョンリスト（特定のチャネルに限定されない広範なバージョン）が更新され、利用可能なバージョンが追加・更新されました。同様に、GKEノードのバージョンも更新され、古いバージョンが利用不可になりました。
影響有無: **影響なし**。Google Cloud ComposerのGKEクラスタはGoogleによって完全に管理されており、基盤GKEバージョンの更新は透過的に行われます。Airflow環境の安定性と互換性はGoogleによって保証されています。
対処方法: 特になし。

## Changed
原文:
**Note**: Your clusters might not have these versions available.
Rollouts are already in progress when we publish the release notes, and can take
multiple days to complete across all Google Cloud zones.

- Version 1.34.1-gke.3355002 is now the default version for cluster creation in the Rapid channel.
- The following versions are now available in the Rapid channel:
    - 1.31.14-gke.1081000
    - 1.32.9-gke.1632000
    - 1.33.5-gke.1956000
    - 1.34.1-gke.3355002
    - 1.34.1-gke.3403002
    - 1.34.1-gke.3556000

- The following versions are no longer available in the Rapid channel:
    - 1.31.13-gke.1231000
    - 1.31.13-gke.1377000
    - 1.32.9-gke.1330000
    - 1.32.9-gke.1462000
    - 1.34.1-gke.3355001
    - 1.34.1-gke.3403001

- Clusters in this channel running the listed minor version have new general auto-upgrade targets. GKE can upgrade control planes and nodes to the following new versions with this release:

- GKE upgrades clusters to the following new minor versions if there are no factors, such as maintenance exclusions or deprecated APIs, preventing upgrades:
    - 1.33 to 1.34.1-gke.3355002

- GKE upgrades clusters to the following new patch versions if no minor version upgrade is available, or if the cluster has maintenance exclusions or other factors preventing minor version upgrades:
    - 1.34 to 1.34.1-gke.3355002

[1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
[1.31.14-gke.1081000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md#v13114)
[1.32.9-gke.1632000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md#v1329)
[1.33.5-gke.1956000](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md#v1335)
[1.34.1-gke.3355002](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md#v1341)
[1.34.1-gke.3403002](https://github.